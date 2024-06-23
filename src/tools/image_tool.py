import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.groq import Groq
from src.utils.llm_utils import load_model
from src.tools.image_analysis.tool import ImageAnalysisToolSuite

def load_image_tool(path="../../dataset/id_1.png"):
  llm = load_model()
  tool_suite = ImageAnalysisToolSuite(image_path=path, llm=llm)
  return tool_suite.get_tools()
