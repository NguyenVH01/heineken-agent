from PIL import Image
from src.agents.image_agent.const import ImageAnalysisAction
import chainlit as cl

class ImageAgent:
  def __init__(self, llm):
    from src.agents.llm_compiler_agent.agent import LLMCompilerAgent
    self._llm = llm
    self._image_path = LLMCompilerAgent._image_path

  def read_image(self):
    image = Image.open(self._image_path)
    return image

  async def process(self, prompt, action: ImageAnalysisAction):
    image = self.read_image()
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
