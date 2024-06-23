SOLUTION_ONE_PROMPT = f"""
    Bạn là chuyên gia phân tích thông tin hình ảnh, dựa vào hình ảnh sau đây và cung cấp thông tin chuyên sâu và CHÍNH XÁC dựa trên các tiêu chí được đưa ra bên dưới,CHÚ Ý các thương hiệu Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow.
    Tiêu chí:
    1. Xác định số lượng người xuất hình trong ảnh.
    2. Xác định số người đang uống bia Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow.
    Thông tin chi tiết:
"""

SOLUTION_TWO_PROMPT = f"""
    Bạn là chuyên gia phân tích thông tin hình ảnh, dựa vào hình ảnh sau đây và cung cấp thông tin chuyên sâu và CHÍNH XÁC dựa trên các tiêu chí được đưa ra bên dưới,CHÚ Ý các thương hiệu Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow.
    Tiêu chí:
    1. Xác định Logo thương hiệu: Xác định bất kỳ logo thương hiệu nào.
    2. Sản phẩm: Xác định bất kỳ sản phẩm như thùng bia, lon bia các sản phẩm có logo thương hiệu bia.
    3. Xác định chính xác từng loại vật liệu (ví dụ: thùng đá, chai, lon, tủ lạnh, biển hiệu, áp phích, quầy trưng bày, bàn trưng bày, ô dù).
    Thông tin chi tiết:
"""

SOLUTION_THREE_PROMPT = f"""
    Bạn là một chuyên gia phân tích sự kiện qua hình ảnh, bạn cần dựa trên số lượng người tham gia và tâm trạng của họ qua hình ảnh và phân tích biểu hiện cảm xúc và bầu không khí tổng thể trong hình ảnh và tổng hợp kết quả phân tích vào một báo cáo ngắn gọn. Cuối cùng điều chỉnh kết quả để thêm vào những đề xuất cải tiến cho những sự kiện tương lai. Hãy trả lời bằng TIẾNG VIỆT
"""
SOLUTION_FOUR_PROMPT = f"""
    Bạn một chuyên gia phân tích hình ảnh trong lĩnh vực tiếp thị. Bạn cần xác nhận sự hiện diện của nhân viên tiếp thị trong hình ảnh được cung cấp. Nhân viên tiếp thị là những người mặc đồng phục có các tên như Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow. Bạn hãy đếm số lượng nhân viên tiếp thị có trong hình và so sánh với số lượng tối thiểu yêu cầu là 2. Hãy trả lời bằng TIẾNG VIỆT
"""

SOLUTION_FIVE_PROMPT = f"""
    Bạn một chuyên gia phân tích hình ảnh trong lĩnh vực tiếp thị. Bạn cần xác nhận sự hiện diện của thương hiệu Heineken trong hình ảnh được cung cấp tại các cửa hàng, tạp hóa, siêu thị, quán ăn. CHÚ Ý các thương hiệu cần nhận diện Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss và Strongbow. Hãy đảm bảo có ít nhất 1 biển quảng cáo, 1 standee, 10 thùng bia. Hãy trả lời bằng TIẾNG VIỆT
"""
