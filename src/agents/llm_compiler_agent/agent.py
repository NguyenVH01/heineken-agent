from typing import List
import chainlit as cl
import pandas as pd
from llama_index.core.agent import AgentRunner, ReActAgent
from llama_index.core.base.llms.types import ChatMessage, MessageRole
from dotenv import load_dotenv
from src.agents.image_agent.image_agent_tool import ImageAgent
from src.agents.base import BaseChainlitAgent
from src.utils.llm_utils import load_model
from .prompts import WELCOME_MESSAGE, BASE_SYSTEM_PROMPT, SYSTEM_PROMPT
from src.agents.image_agent.const import ImageAnalysisAction
from src.agents.image_agent.prompt import SOLUTION_TWO_PROMPT, SOLUTION_THREE_PROMPT, SOLUTION_FOUR_PROMPT, SOLUTION_FIVE_PROMPT

load_dotenv(override=True)

class LLMCompilerAgent(BaseChainlitAgent):

  _agent: AgentRunner
  _image_path: str
  _AGENT_IDENTIFIER: str = "LLMAnalyzerAgent"
  _HISTORY_IDENTIFIER: str = f"{_AGENT_IDENTIFIER}_chat_history"
  _image_agent: ImageAgent

  # @staticmethod
  # def _get_chat_history() -> list[dict]:
  #   chat_history = cl.user_session.get(
  #       key=LLMCompilerAgent._HISTORY_IDENTIFIER, default=[])
  #   return chat_history

  # @staticmethod
  # def _set_chat_history(chat_history: list[dict]) -> None:
  #   cl.user_session.set(
  #       key=LLMCompilerAgent._HISTORY_IDENTIFIER, value=chat_history)

  # @classmethod
  # def _construct_message_history(self, message_history: List[dict] = None) -> List[ChatMessage]:
  #   self._agent.memory.reset()
  #   memory = [
  #       ChatMessage(content=BASE_SYSTEM_PROMPT, role=MessageRole.SYSTEM),
  #       ChatMessage(content=SYSTEM_PROMPT, role=MessageRole.SYSTEM),
  #   ]

  #   if message_history:
  #     memory.extend([ChatMessage(**message) for message in message_history])

  #   self._agent.memory.set(messages=memory)
  #   return memory

  # @classmethod
  # def _init_tools(cls):
  #   from src.tools.image_tool import load_image_tool
  #   return load_image_tool(path=LLMCompilerAgent._image_path)

  @classmethod
  async def _load_action_menu(cls):
    actions = [
        cl.Action(name=ImageAnalysisAction.SOLUTION_ONE.value, value="solution1",
                  description="Vấn đề kinh doanh 1"),
        cl.Action(name=ImageAnalysisAction.SOLUTION_TWO.value, value="solution2",
                  description="Vấn đề kinh doanh 2"),
        cl.Action(name=ImageAnalysisAction.SOLUTION_THREE.value, value="solution3",
                  description="Vấn đề kinh doanh 3"),
        cl.Action(name=ImageAnalysisAction.SOLUTION_FOUR.value, value="solution4",
                  description="Vấn đề kinh doanh 4"),
        cl.Action(name=ImageAnalysisAction.SOLUTION_FIVE.value, value="solution5",
                  description="Vấn đề kinh doanh 5"),
        cl.Action(name=ImageAnalysisAction.ANALYZE_NEW.value, value="analyze_new",
                  description="Phân tích hình ảnh mới"),
    ]
    await cl.Message(content="Hãy chọn các vấn đề bạn muốn phân tích:", actions=actions).send()

  @classmethod
  async def _ask_file_handler(cls):
    files = None

    # Wait for the user to upload a file
    while files == None:
      files = await cl.AskFileMessage(
          content=WELCOME_MESSAGE,
          accept={'image/jpeg': ['.jpeg', '.png']},
          max_size_mb=25
      ).send()

    image = files[0]
    LLMCompilerAgent._image_path = image.path
    result_image = cl.Image(path=image.path, name="image", display="inline")

    await cl.Message(f"File uploaded successfully! Ask anything about the data!", elements=[result_image]).send()

    return image.path

  @classmethod
  async def aon_start(cls, *args, **kwargs):
    # LLMCompilerAgent._set_chat_history([])\
    path = await LLMCompilerAgent._ask_file_handler()
    llm = load_model()
    LLMCompilerAgent._image_agent = ImageAgent(llm=llm)

    await LLMCompilerAgent._load_action_menu()

    # tools = LLMCompilerAgent._init_tools()
    # agent = ReActAgent.from_tools(
    #     tools, llm=llm, verbose=True, max_iterations=MAX_ITERATIONS
    # )
    # LLMCompilerAgent._agent = agent
    # cl.user_session.set(LLMCompilerAgent._AGENT_IDENTIFIER, agent)

  @classmethod
  async def aon_message(cls, message: cl.Message, *args, **kwargs):
    await LLMCompilerAgent._image_agent.process(message.content)

  @cl.action_callback(ImageAnalysisAction.SOLUTION_ONE.value)
  async def on_action(action: cl.Action):
    await LLMCompilerAgent._image_agent.process(
        None, ImageAnalysisAction.SOLUTION_ONE)

  @cl.action_callback(ImageAnalysisAction.SOLUTION_TWO.value)
  async def on_action(action: cl.Action):
    await LLMCompilerAgent._image_agent.process(
        SOLUTION_TWO_PROMPT, ImageAnalysisAction.SOLUTION_TWO)

  @cl.action_callback(ImageAnalysisAction.SOLUTION_THREE.value)
  async def on_action(action: cl.Action):
    await LLMCompilerAgent._image_agent.process(
        SOLUTION_THREE_PROMPT, ImageAnalysisAction.SOLUTION_THREE)

  @cl.action_callback(ImageAnalysisAction.SOLUTION_FOUR.value)
  async def on_action(action: cl.Action):
    await LLMCompilerAgent._image_agent.process(
        SOLUTION_FOUR_PROMPT, ImageAnalysisAction.SOLUTION_FOUR)

  @cl.action_callback(ImageAnalysisAction.SOLUTION_FIVE.value)
  async def on_action(action: cl.Action):
    await LLMCompilerAgent._image_agent.process(
        SOLUTION_FIVE_PROMPT, ImageAnalysisAction.SOLUTION_FIVE)

  @cl.action_callback(ImageAnalysisAction.ANALYZE_NEW.value)
  async def on_action(action: cl.Action):
    path = await LLMCompilerAgent._ask_file_handler()
    LLMCompilerAgent._image_path = path
    await LLMCompilerAgent._load_action_menu()
