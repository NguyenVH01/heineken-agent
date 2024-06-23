import os
# from llama_index.llms.groq import Groq
# from llama_index.llms.openai import OpenAI
# from llama_index.llms.ollama import Ollama
# from llama_index.llms.gemini import Gemini
# from llama_index.multi_modal_llms.gemini import GeminiMultiModal
# from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from src.const import LLM_PROVIDER, MODEL_ID, TEMPERATURE
import google.generativeai as genai
import logging

def load_baseline_llm():
  if LLM_PROVIDER == "gemini":
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai

def load_model():
  """
  Select a model for text generation using multiple services.
  Args:
      LLM_PROVIDER (str): Service name indicating the type of model to load.
      MODEL_ID (str): Identifier of the model to load from HuggingFace's model hub.
  Returns:
      LLM: llama-index LLM for text generation
  Raises:
      ValueError: If an unsupported model or device type is provided.
  """
  logging.info(f"Loading Model: {MODEL_ID}")
  logging.info("This action can take a few minutes!")

  if LLM_PROVIDER == "gemini":
    logging.info(f"Loading Gemini Model: {MODEL_ID}")
    generation_config = {
        "temperature": 0.8,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    return genai.GenerativeModel(model_name=MODEL_ID, generation_config=generation_config,
                                 )
  else:
    raise NotImplementedError(
        "The implementation for other types of LLMs are not ready yet!")
