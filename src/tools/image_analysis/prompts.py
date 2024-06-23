from llama_index.core.prompts import PromptTemplate, PromptType

DEFAULT_INSTRUCTION_STR = (
    "1. Logo thương hiệu: Xác định bất kỳ logo thương hiệu nào \n"
    "2. Sản phẩm: Xác định bất kỳ sản phẩm như thùng bia, lon bia các sản phẩm có logo thương hiệu bia\n"
)

DEFAULT_IMAGE_TMPL = (
    "Bạn là chuyên gia phân tích thông tin hình ảnh, dựa vào hình ảnh sau đây và cung cấp thông tin chuyên sâu dựa trên các tiêu chí được đưa ra bên dưới,CHÚ Ý các thương hiệu Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow.\n"
    "Tiêu chí:\n"
    "{instruction_str}\n"
    "Thông tin chi tiết:"
)

DEFAULT_IMAGE_PROMPT = PromptTemplate(
    DEFAULT_IMAGE_TMPL, prompt_type=PromptType.SIMPLE_INPUT
)
