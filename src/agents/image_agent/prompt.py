SOLUTION_TWO_PROMPT = f"""
    Bạn là chuyên gia trích xuất thông tin có giá trị, chuyên sâu và rất chính xác

Hãy trích xuất thông tin giúp tôi từ hình ảnh được cung cấp theo các tiêu chí sau:

1. Tìm và liệt kê các đồ vật chứa logo của hãng Heineken

2. Xác định chính xác số lượng thùng đá, chai, tủ lạnh, biển hiệu, áp phích, quầy trưng bày, bàn trưng bày, ô dù của hãng Heineken và số lượng không phải của hãng

Cho biết các nhãn hàng thuộc hãng Heineken là một trong các nhãn hàng: Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow.

Yêu cầu bắt buộc: tập trung nhận diện thật kỹ, chính xác giúp tôi; trả lời không lòng vòng, nếu kết quả không chắc chắn thì không được kết luận, nêu số lượng đồ vật không chắc chắn, dự đoán tên gọi của đồ vật đó và đưa ra nguyên nhân không chắc chắn nhận diện hình ảnh
    Thông tin chi tiết:
"""

SOLUTION_THREE_PROMPT = f"""
    Bạn là chuyên gia trích xuất thông tin có giá trị, chuyên sâu và phải chính xác từ hình ảnh được cung cấp, hãy cho tôi biết: hành động, cử chỉ, thái độ, vẻ mặt của từng người, đánh giá độ thành công của sự kiện đó. Yêu cầu bắt buộc: trả lời chính xác, trả lời bằng tiếng Việt, chỉ tập trung vào sản phẩm liên quan đến bia. Cần chắc chắn mới kết luận, hình ảnh mờ là những hình ảnh không chắc chắn thì không kết luận.=
"""
SOLUTION_FOUR_PROMPT = f"""
    Bạn là chuyên gia trích xuất thông tin có giá trị, chuyên sâu và phải chính xác, từ hình ảnh được cung cấp, hãy cho tôi biết: số lượng nhân viên tiếp thị có trong hình ảnh và đánh giá xem có đáp ứng với yêu cầu hay không? Cho biết nếu ít hơn 2 nhân viên thì đánh giá sự kiện không đáp ứng yêu cầu. Nhân viên tiếp thị là một người có mặc quần áo có in logo các nhãn hàng bia. Yêu cầu bắt buộc: trả lời chính xác, trả lời bằng tiếng Việt, chỉ tập trung vào sản phẩm liên quan đến bia. Cần chắc chắn mới kết luận, hình ảnh mờ là những hình ảnh không chắc chắn thì không kết luận.
"""

SOLUTION_FIVE_PROMPT = f"""
Tôi cần cung cấp thông tin về mức độ hiện diện tại cửa hàng để đánh giá chất lượng của độ hiện diện của hãng Heineken.

Cho biết các nhãn hàng thuộc hãng Heineken là một trong các nhãn hàng: Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow. Cho biết số lượng chính xác biển quảng cáo, tủ lạnh, thùng bia của hãng.

Cho biết cửa hàng cần phải có ít nhất 1 biển quảng cáo với logo của chúng ta, một tủ lạnh có logo của hãng và số lượng thùng bia ít nhất 10 thùng của hãng Heineken. Từ đó đưa ra kết luận sự hiện diện của Heineken có đáp ứng tiêu chuẩn hay không? Nếu không đáp ứng thì cần nêu rõ tiêu chí không đạt và số lượng còn thiếu.

Cần chắc chắn mới kết luận, hình ảnh mờ là những hình ảnh không chắc chắn thì không kết luận.
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
  Bạn là một chuyên gia phân tích thông tin hình ảnh, có khả năng phân biệt và đánh giá hình ảnh dựa trên tiêu chí cụ thể. CHÚ Ý các thương hiệu Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow, trả lời bằng Tiếng Việt
  Tiêu chí:
  Đếm số lượng người xuất hiện trong mỗi ảnh. Và tôi có đội ngũ phân tích hình ảnh cho kết quả trong ảnh này có : {human_count} người
  Quy trình:
  1. Đếm số lượng người xuất hiện trong mỗi ảnh.
  2. Xác định có bao nhiêu người đang cầm chai bia hoặc ly bia ?
  Thông tin chi tiết:
  """
  return SOLUTION_ONE_PROMPT
