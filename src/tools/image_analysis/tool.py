import logging
import pandas as pd
from llama_index.core.llms import LLM
from llama_index.core.base.response.schema import Response
from llama_index.core.tools import FunctionTool
from src.tools.image_analysis.prompts import (
    DEFAULT_IMAGE_PROMPT,
    DEFAULT_INSTRUCTION_STR
)
import chainlit as cl
from chainlit import run_sync
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls

class ImageAnalysisToolSuite:

  def __init__(self, image_path: str, llm: LLM) -> None:
    self._llm = llm
    self._image_path = image_path
    self._image_prompt = DEFAULT_IMAGE_PROMPT
    self._instruction_str = DEFAULT_INSTRUCTION_STR
    self._verbose = True
    self._synthesize_response = False

  def image_analysis(self) -> dict:
    image_urls = [
        self._image_path
    ]

    image_documents = load_image_urls(image_urls)

    image_output = self._llm.stream_complete(
        prompt=self._image_prompt, image_documents=image_documents)
    if self._verbose:
      logging.info(f"> Execution Output: {image_output}\n")
      run_sync(cl.Message(content=f"Execution Output: \n {
               image_output}\n").send())

    response_metadata = {
        "raw_image_output": image_output,
    }

    return Response(response=image_output, metadata=response_metadata)

  def get_tools(self):
    """Get tools."""
    return [
        FunctionTool.from_defaults(fn=self.image_analysis),
    ]
