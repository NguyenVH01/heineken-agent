from PIL import Image
from src.agents.image_agent.const import ImageAnalysisAction
import chainlit as cl
import json
import random
import io
from PIL import Image, ImageDraw
from PIL import ImageColor

class ImageAgent:
  def __init__(self, llm):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    self._llm = llm
    self._image_path = LLMCompilerAgent._image_path
    self._additional_colors = [colorname for (colorname, colorcode) in ImageColor.colormap.items()]

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
    ] + additional_colors

    # Iterate over the noun phrases and their positions
    for i, (noun_phrase, (y1, x1, y2, x2)) in enumerate(
        noun_phrases_and_positions):
        # Select a color from the list
        color = colors[i % len(colors)]

        # Convert normalized coordinates to absolute coordinates
        abs_x1 = int(x1/1000 * width)
        abs_y1 = int(y1/1000 * height)
        abs_x2 = int(x2/1000 * width)
        abs_y2 = int(y2/1000 * height)

        # Draw the bounding box
        draw.rectangle(
            ((abs_x1, abs_y1), (abs_x2, abs_y2)), outline=color, width=4
        )

        # Draw the text
        draw.text((abs_x1 + 8, abs_y1 + 6), noun_phrase, fill=color)

    # Return the image
    return img

  def read_image(self):
    image = Image.open(self._image_path)
    return image
  
  # async def object_detection(self):
  #   pass

  async def process(self, prompt, action: ImageAnalysisAction):
    image = self.read_image()
    # if action.value == ImageAnalysisAction.SOLUTION_ONE.value:

    response = self._llm.generate_content([prompt, image])

    result = f"""
      > ## Kết quả {action.value}:
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
