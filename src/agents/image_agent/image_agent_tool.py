from PIL import Image
import chainlit as cl

from src.const import SOLUTION_ONE, SOLUTION_TWO, SOLUTION_THREE, SOLUTION_FOUR, SOLUTION_FIVE

class ImageAgent:
  def __init__(self, llm):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    self._llm = llm
    self._image_path = LLMCompilerAgent._image_path

  def read_image(self):
    image = Image.open(self._image_path)
    return image

  async def process(self, prompt):
    image = self.read_image()
    response = self._llm.generate_content([prompt, image])
    print(response.text)

    image = cl.Image(path=self._image_path, name="image", display="inline")
    await cl.Message(f"File uploaded successfully! Ask anything about the data!", elements=[image]).send()
    actions = [
        cl.Action(name=SOLUTION_ONE, value="solution1",
                  description="Vấn đề kinh doanh 1"),
        cl.Action(name=SOLUTION_TWO, value="solution2",
                  description="Vấn đề kinh doanh 2"),
        cl.Action(name=SOLUTION_THREE, value="solution3",
                  description="Vấn đề kinh doanh 3"),
        cl.Action(name=SOLUTION_FOUR, value="solution4",
                  description="Vấn đề kinh doanh 4"),
        cl.Action(name=SOLUTION_FIVE, value="solution5",
                  description="Vấn đề kinh doanh 5"),
    ]

    await cl.Message(content="Hãy chọn các vấn đề bạn muốn phân tích:", actions=actions).send()

    return response.text
