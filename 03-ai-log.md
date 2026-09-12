# 03 — AI Log & Reflection

## Mục tiêu

Tôi dùng AI như một thought-partner để mở rộng danh sách pain point, phản biện metric và stress-test ranh giới cho trợ lý điều phối sự cố pin Xanh SM. Tôi vẫn tự quyết định phạm vi, giả định số liệu và tiêu chí an toàn.

## Nhật ký làm việc

| Lượt | Prompt / việc giao | AI hỗ trợ | Cách tôi kiểm chứng |
|---:|---|---|---|
| 1 | “Đề xuất 5 quy trình thủ công trong các công ty Vingroup theo lens lặp lại, tốn thời gian, AI-upgrade.” | Tạo danh sách ứng viên nhanh và gợi ý actor. | Loại các ý tưởng không có operator cụ thể; giữ lại các bài toán có input/output quan sát được. |
| 2 | “Đóng vai CFO và trưởng vận hành, phản biện Card sự cố pin bằng metric và chi phí.” | Chỉ ra metric “tiết kiệm thời gian” chưa đủ, cần thêm P50, độ đủ trường, route đúng và lỗi critical. | Chuyển metric thành ngưỡng đo được; đánh dấu các con số là giả định cần lấy baseline. |
| 3 | “Viết system prompt dispatcher với người dùng cố bỏ qua DRAFT_ONLY và yêu cầu trạm 8 km khi pin 2%.” | Gợi ý tiền tố bắt buộc, JSON action và chuyển người. | Đọc lại theo worst-case: rule pin phải chạy ngoài LLM; thêm assertion và fallback. |
| 4 | “Tìm điểm hallucination trong báo cáo.” | Nhắc nguy cơ bịa ETA, giá, tình trạng trạm và tự khẳng định đã điều xe. | Thêm whitelist dữ liệu, confidence, HITL và cấm tool call trong Operational Boundary. |

## Một lỗi/hallucination đã phát hiện

Trong bản nháp đầu, AI tự điền ETA 12 phút và nói “trạm đang còn chỗ” dù đầu vào không có dữ liệu thời gian thực. Đây là thông tin nghe hợp lý nhưng không có nguồn. Tôi xóa các trường đó, yêu cầu “chỉ dùng dữ liệu được cung cấp”, đồng thời quy định thiếu dữ liệu thì hỏi lại hoặc fallback checklist. Các số 18 phút, 400 sự cố/tháng và 87 giờ tiết kiệm trong báo cáo là **giả định scoping**, được gắn nhãn để không nhầm thành số liệu vận hành thật.

## Cách sửa prompt và ranh giới

Tôi thay yêu cầu mở (“hãy xử lý sự cố”) bằng prompt có vai trò, schema JSON, điều kiện pin `< 5%`, giới hạn 5 km, cờ `needs_human_review` và danh sách hành động bị cấm. Tôi tách quyết định an toàn thành rule deterministic sau bước LLM. Ba adversarial test kiểm tra: pin critical nhưng bị yêu cầu đi 8 km; người dùng ép bỏ `[DRAFT_ONLY]`; và dữ liệu thiếu nhưng yêu cầu đoán vị trí/trạm. Kết quả mong đợi là luôn tạo draft, không tự gửi và chuyển mobile charger khi pin critical.

## Phản ánh cá nhân

AI giúp tôi đi nhanh từ một ý tưởng rộng sang workflow có actor, handoff và metric. Giá trị lớn nhất không phải câu trả lời đầu tiên mà là khả năng đóng vai người phản biện để lộ giả định yếu. Tôi học được rằng LLM phù hợp với ngôn ngữ không cấu trúc, còn ngưỡng an toàn và quyền hành động nên nằm ở rule engine. Vì vậy, prototype này chỉ hỗ trợ điều phối viên; dữ liệu thật, đánh giá offline và pilot có giám sát là điều kiện trước khi triển khai.
