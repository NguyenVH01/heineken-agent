SOLUTION_TWO_PROMPT = f"""
    You are an expert at extracting valuable, in-depth, and very accurate information

Please help me extract information from the provided image according to the following criteria:

1. Find and list objects containing the Heineken brand logo

2. Determine the exact number of ice boxes, bottles, refrigerators, signs, posters, display counters, display tables, and umbrellas of the Heineken brand and the number of non-Heineken brands

Indicate that the brands belonging to Heineken are among the brands: Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow.

Requirements: focus on identifying carefully and accurately, help me; answer without beating around the bush, if the result is uncertain then do not conclude, state the number of uncertain objects, predict the name of that object, and give the cause of uncertainty identify the image, answer in English
 Details Description:
"""

SOLUTION_THREE_PROMPT = f"""
    You are an expert in extracting valuable, in-depth, and accurate information from the provided images, please tell me: the actions, gestures, attitudes, and facial expressions of each person, and the assessment of the event's success. Requirements: answer correctly, and only focus on beer-related products. It would help if you were sure to conclude. Blurred images are uncertain images and cannot be concluded.
"""
SOLUTION_FOUR_PROMPT = f"""
    You are an expert in extracting valuable, in-depth, and accurate information, from the image provided, please tell me: the number of marketing staff in the image and evaluate whether it meets the requirements demand or not. Indicates that the event that meets the requirement needs to be greater than or equal to 2 marketing staff. A marketing staff is a person who wears clothes with beer brand logos printed on them. Mandatory requirements: answer correctly, and only focus on beer-related products. It would help if you were certain to conclude, that blurry images are uncertain images and are not conclusive.
"""

SOLUTION_FIVE_PROMPT = f"""
I need to provide information about the level of presence in the store to evaluate the quality of Heineken's presence.

Indicate that the brands belonging to Heineken are among the brands: Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow. Indicate the exact number of print advertising, standee, and beer crates of the company.

Indicate that the store needs to have at least 1 print advertising with the Heineken logo, a standee with the company's logo, and at least 10 crates of Heineken beer. From there, we can conclude whether Heineken's presence meets the standards or not. If not met, it is necessary to clearly state the failure criteria and the missing quantity.

It would help if you were certain to conclude, that blurry images are uncertain images and are not conclusive.
"""

HUMAN_DETECTION_PROMPT = """
Bạn là một chuyên gia phân tích thông tin hình ảnh, có khả năng phân biệt và đánh giá hình ảnh dựa trên tiêu chí cụ thể. 
Bạn hãy xác định người xuất hiện trong ảnh và trả về kết quả các định dạng như sau: {'object_0' : [ymin, xmin, ymax, xmax], ...}  Nếu có nhiều hơn một phiên bản của một đối tượng, hãy thêm chúng vào từ điển dưới dạng 'object_0', 'object_1', v.v. Nếu không tìm thấy không trả ra kết quả
"""

OBJECT_DETECTION_PROMPT = """
Bạn là một chuyên gia phân tích thông tin hình ảnh, có khả năng phân biệt và đánh giá hình ảnh dựa trên tiêu chí cụ thể. CHÚ Ý các thương hiệu Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow. Và tôi có đội ngũ phân tích bộ nhận dạng thương hiệu logo cung cấp dữ liệu nhận dạng như sau: "
Bia Việt: Logo gồm một con chim én trắng bay về phía bên phải, tạo hình ngôi sao vàng, và chữ "BIA VIET" màu đen đậm trên nền đỏ.
Bivinia: Logo là một vòng tròn trắng có viền đỏ, bên trong có chữ "BIVINIA" màu đen, được tô viền màu trắng, chữ "LAGER BEER" màu đen nằm ở phía dưới. Phía trên vòng tròn là dòng chữ "TRADE MARK" màu đen với một ngôi sao vàng ở giữa. Vòng tròn được bao quanh bởi hai bông lúa mì vàng.
Edelweiss: Logo bao gồm một bông hoa Edelweiss, được bao quanh bởi dòng chữ "BORN IN THE ALPS 1846", bên dưới là dòng chữ "Edelweiss" được in theo kiểu chữ Gothic.
Heineken: Logo Heineken bao gồm một ngôi sao đỏ năm cánh, bên dưới là dòng chữ "EST. 1873", và chữ "Heineken" được in đậm. Bên phải chữ "Heineken" là một vòng tròn chứa chữ "R".
Larue: Logo có hình đầu hổ với màu cam và vàng, với đôi mắt xanh dương và chiếc mũi đen, trên nền đen. Dưới đầu hổ là một dải băng màu xanh lá cây với dòng chữ "LARUE" màu vàng, bên dưới là dòng chữ "SPECIAL" màu trắng và hình ảnh hai bông lúa mì màu vàng.
Strongbow: Logo có chữ strongbow
Tiger: Logo có hình một con hổ màu vàng với sọc màu nâu, đang ngồi với tư thế uy nghi. Bên dưới là dòng chữ "Tiger"
"
Bạn hãy xác định các lon bia và chai bia và người xuất hiện trong ảnh và trả về kết quả các định dạng như sau: {'object_0' : [ymin, xmin, ymax, xmax], ...}  Nếu có nhiều hơn một phiên bản của một đối tượng, hãy thêm chúng vào từ điển dưới dạng 'object_0', 'object_1', v.v. Nếu không có chai bia hoặc lon bia thì không trả ra kết quả
"""


def detection_human(human_count):
  SOLUTION_ONE_PROMPT = f"""
  You are an expert in analyzing visual information, capable of distinguishing and evaluating images based on specific criteria.
  Criteria:
  Count the number of people appearing in each photo. And I have an image analysis team that gives results in this image: {human_count} people. If not met, it is necessary to clearly state the failure criteria and the missing quantity.
  Procedure:
  1. Count the number of people appearing in each photo.
  2. Determine how many people drinking beer whose holding beer bottles or beer glasses?
  Details:
  """
  return SOLUTION_ONE_PROMPT
