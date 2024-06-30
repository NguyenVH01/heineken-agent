from PIL import Image
from src.agents.image_agent.const import ImageAnalysisAction
import chainlit as cl
import json
from PIL import Image, ImageDraw
from PIL import ImageColor
import numpy as np
import io
from src.agents.image_agent.prompt import HUMAN_DETECTION_PROMPT, detection_human
import matplotlib.pyplot as plt
import numpy as np

class ImageAgent:
  def __init__(self, llm):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    self._llm = llm
    self._image_path = LLMCompilerAgent._image_path
    self._additional_colors = [colorname for (
        colorname, colorcode) in ImageColor.colormap.items()]
    self.bbox_str = None
    self.bbox_hist = ''

  def parse_list_boxes(self, text):
    result = []
    for line in text.strip().splitlines():
      # Extract the numbers from the line, remove brackets and split by comma
      try:
        numbers = line.split('[')[1].split(']')[0].split(',')
      except:
        numbers = line.split('- ')[1].split(',')

      # Convert the numbers to integers and append to the result
      result.append([int(num.strip()) for num in numbers])

    return result

  def parse_list_boxes_with_label(self, text):
    text = text.split("```\n")[0]
    return json.loads(text.strip("```").strip("python").strip("json").replace("'", '"').replace('\n', '').replace(',}', '}'))

  def postproc_bbox_str(self, height, width):
    x0, y0, x1, y1 = [float(x) for x in self.bbox_str.removeprefix(
        '[').removesuffix(']').split(',')]
    x0 = int(np.round(x0 / width * 1000))
    y0 = int(np.round(y0 / height * 1000))
    x1 = int(np.round(x1 / width * 1000))
    y1 = int(np.round(y1 / height * 1000))
    return f'{y0} {x0} {y1} {x1}'

  def postproc_bbox_hist(self, height, width):
    bbox_strs = self.bbox_hist.rstrip().split("\n")
    results = []
    for bbox_str in bbox_strs:
      x0, y0, x1, y1 = [float(x) for x in bbox_str.removeprefix(
          '[').removesuffix(']').split(',')]
      x0 = int(np.round(x0 / width * 1000))
      y0 = int(np.round(y0 / height * 1000))
      x1 = int(np.round(x1 / width * 1000))
      y1 = int(np.round(y1 / height * 1000))
      results.append(f" (x = {(x0 + x1) // 2}, y = {(y0 + y1) // 2}); ")
    return results

  def plot_bounding_boxes(self, noun_phrases_and_positions):
    """
    Plots bounding boxes on an image with markers for each noun phrase, using PIL, normalized coordinates, and different colors.

    Args:
        img_path: The path to the image file.
        noun_phrases_and_positions: A list of tuples containing the noun phrases
         and their positions in normalized [y1 x1 y2 x2] format.
    """

    # Load the image
    img = self.read_image()
    width, height = img.size
    print(img.size)
    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a list of colors
    colors = [
        'red',
        'green',
        'blue',
        'yellow',
        'orange',
        'pink',
        'purple',
        'brown',
        'gray',
        'beige',
        'turquoise',
        'cyan',
        'magenta',
        'lime',
        'navy',
        'maroon',
        'teal',
        'olive',
        'coral',
        'lavender',
        'violet',
        'gold',
        'silver',
    ] + self._additional_colors

    # Iterate over the noun phrases and their positions
    for i, (noun_phrase, (y1, x1, y2, x2)) in enumerate(
            noun_phrases_and_positions):
        # Select a color from the list
      color = colors[i % len(colors)]

      # Convert normalized coordinates to absolute coordinates
      abs_x1 = int(x1 / 1000 * width)
      abs_y1 = int(y1 / 1000 * height)
      abs_x2 = int(x2 / 1000 * width)
      abs_y2 = int(y2 / 1000 * height)

      # Draw the bounding box
      draw.rectangle(
          ((abs_x1, abs_y1), (abs_x2, abs_y2)), outline=color, width=8
      )

      # Draw the text
      draw.text((abs_x1 + 8, abs_y1 + 6), noun_phrase, fill=color)

    # Return the image

    return self.image_to_byte_array(img)

  def image_to_byte_array(self, image: Image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=image.format)
    image_bytes = image_bytes.getvalue()
    return image_bytes

  def read_image(self):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    image = Image.open(LLMCompilerAgent._image_path)
    return image

  async def object_detection(self, image):
    response = self._llm.generate_content([HUMAN_DETECTION_PROMPT, image])
    boxes = self.parse_list_boxes_with_label(response.text)

    detection_img = self.plot_bounding_boxes(
        noun_phrases_and_positions=list(boxes.items()))

    image = cl.Image(content=detection_img, name="image", display="inline")
    await cl.Message(f"> ## Evaluate human detection:", elements=[image]).send()

    return len(boxes.keys())

  async def process(self, prompt, action: ImageAnalysisAction):
    image = self.read_image()

    if action.value == ImageAnalysisAction.SOLUTION_ONE.value:
      human_count = await self.object_detection(image)
      prompt = detection_human(human_count)

    print(prompt)
    response = self._llm.generate_content([prompt, image])

    result = f"""
      > ## Evaluate {action.value}:
{response.text}
    """
    print(result)

    message = cl.Message(result)

    # image = cl.Image(path=self._image_path, name="image", display="inline")
    # await cl.Message(f"File uploaded successfully! Ask anything about the data!", elements=[image]).send()

    await message.send()

    await self.show_action_buttons()

  async def show_action_buttons(self):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    await LLMCompilerAgent._load_action_menu()
