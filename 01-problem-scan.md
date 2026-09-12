# Phase 1–2 — Problem Scan & Quick Assessment

Người nộp: **v1rtuos024** · Branch cá nhân: `v1rtuos024` · Ngày: 12/09/2026.

## Phạm vi và nguồn thông tin

Bài làm sử dụng bối cảnh giả lập Vin Smart Future trong [worksheet](01-worksheet.md) và các lĩnh vực nghiệp vụ từ [inspiration kit](03-inspiration-kit.md). Các pain point dưới đây là giả thuyết cần khảo sát tại đơn vị, không phải kết quả phỏng vấn đã thực hiện. Toàn bộ thời gian, sản lượng và mục tiêu định lượng là giả định thiết kế cho bài lab; chưa có logs nội bộ để xác nhận. Không khẳng định cơ cấu tổ chức hoặc năng lực dịch vụ thực tế từ tình huống giảng dạy.

## Phase 1 — SCAN

| # | Công ty / đơn vị trong bối cảnh lab | Lens | Bài toán vận hành cụ thể | Dữ liệu cần xác minh |
|---|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian; stakeholder pain | Điều phối viên phải đọc báo cáo pin thấp, xác minh thông tin và soạn phản hồi; tài xế chờ qua nhiều lần trao đổi. | Ticket sự cố, thời điểm tiếp nhận/phản hồi, mức pin đã xác minh. |
| 2 | Vinhomes | Lặp lại; AI-upgrade | Phản ánh cư dân viết tự do, gộp nhiều vấn đề, khiến CSKH phân loại và chuyển sai đội xử lý. | Ticket đã ẩn danh, nhãn bộ phận, lịch sử chuyển lại. |
| 3 | Vinpearl | Tốn thời gian; AI-upgrade | Nhân viên đọc email đặt phòng đoàn, nhập ngày ở/số phòng và hỏi lại thông tin thiếu. | Email giả lập hoặc đã ẩn danh, biểu mẫu yêu cầu đặt phòng. |
| 4 | VinFast | Lặp lại | Đối chiếu hóa đơn sạc với phiên sạc và tìm chênh lệch bằng tay. Rule đối chiếu mã phiên/số tiền có thể đủ. | Mã phiên, hóa đơn, biểu phí đã được phê duyệt. |
| 5 | Vinmec | Stakeholder pain | Nhân viên hành chính phải trả lời lặp lại câu hỏi về giấy tờ và hướng dẫn chuẩn bị hồ sơ trước lịch hẹn. | FAQ hành chính được duyệt, loại lịch hẹn; không cần bệnh án. |
| 6 | VinWonders | AI-upgrade; stakeholder pain | Nhân viên tổng hợp phản hồi khách về xếp hàng, thiếu chỉ dẫn và tiện ích để chuyển quản lý ca. | Phản hồi đã ẩn danh, khu vực, thời điểm, nhãn vấn đề. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card 1 — Nháp phản hồi sự cố pin Xanh SM

| Trường | Nội dung |
|---|---|
| Bài toán / đơn vị | Rút ngắn xử lý thông tin và soạn nháp khi tài xế Xanh SM báo sự cố pin. |
| Actor | Điều phối viên trực tiếp xử lý; tài xế chịu thời gian chờ; trưởng ca duyệt ngoại lệ. |
| Workflow hiện tại | 1. Nhận báo cáo (2 phút) → 2. Xác minh vị trí/mức pin (2 phút) → 3. Tra cứu phương án hỗ trợ (5 phút) → 4. Soạn và rà soát phản hồi (5 phút) → 5. Gửi/chuyển yêu cầu và ghi log (1 phút). |
| Bottleneck | Bước 3–4: 10/15 phút mỗi lượt; chuyển công cụ và viết lại thông tin. |
| AI Solution | Rule quyết định nhánh theo pin đã xác minh; LLM soạn nháp tiếng Việt; điều phối viên kiểm tra và duyệt. Prototype chỉ kiểm thử nháp, chưa tra cứu hoặc điều xe thực tế. |
| Metric có số | Mục tiêu median từ 15 xuống ≤ 8 phút/lượt; thời gian soạn và duyệt từ 5 xuống ≤ 2 phút; 100% nháp cần người duyệt; 0 đề xuất trạm khi chưa có dữ liệu được xác minh. |
| Dữ liệu / ranh giới | Telemetry do operator nhập trong mô phỏng, tin nhắn tài xế không đáng tin cậy. Pin < 5% phải đề xuất `dispatch_mobile_charger` theo quy tắc bài lab; đây chỉ là nhãn đề nghị hỗ trợ, không khẳng định có xe sạc di động khả dụng. |
| Quick Architecture | Rule + LLM Feature; không Agentic Loop. |
| Cần kiểm chứng | Năng lực hỗ trợ thực tế, baseline thời gian, quyền truy cập và chất lượng dữ liệu pin. |

### Quick Problem Card 2 — Phân loại phản ánh cư dân Vinhomes

| Trường | Nội dung |
|---|---|
| Bài toán / đơn vị | Giảm thời gian phân loại phản ánh cư dân và chuyển đúng bộ phận Vinhomes. |
| Actor | CSKH ban quản lý; đội kỹ thuật/vệ sinh/an ninh; cư dân gửi phản ánh. |
| Workflow hiện tại | 1. Đọc phản ánh (1 phút) → 2. Hỏi bổ sung tòa/khu vực (3 phút thao tác, chưa tính chờ cư dân) → 3. Gán nhãn (2 phút) → 4. Chuyển đội xử lý (1 phút) → 5. Ghi nhận và phản hồi (1 phút). |
| Bottleneck | Bước 2–3 chiếm 5/8 phút thao tác; một tin nhắn có thể chứa nhiều vấn đề hoặc thiếu vị trí. |
| AI Solution | LLM trích xuất vị trí và nhiều nhãn vấn đề, nêu thông tin thiếu; rule ánh xạ nhãn sang danh sách đội phụ trách; CSKH duyệt chuyển. |
| Metric có số | Mục tiêu median thao tác 8 → ≤ 4 phút; macro-F1 nhãn ≥ 0,90 trên 200 ticket do người gán nhãn; tỷ lệ chuyển lại ≤ 5%. |
| Dữ liệu / ranh giới | Ẩn danh cư dân/căn hộ; không tự cam kết phí hoặc thời hạn; sự cố có dấu hiệu khẩn cấp chuyển người trực ngay theo quy trình đã duyệt. |
| Quick Architecture | LLM Feature + Rule router; so sánh với form chọn danh mục và từ khóa trước. |
| Cần kiểm chứng | Danh mục và đội sở hữu ticket, chất lượng nhãn, mức chấp nhận của CSKH. |

### Quick Problem Card 3 — Trích xuất yêu cầu đặt phòng đoàn Vinpearl

| Trường | Nội dung |
|---|---|
| Bài toán / đơn vị | Chuẩn hóa yêu cầu đặt phòng đoàn từ email cho nhân viên đặt phòng Vinpearl. |
| Actor | Nhân viên reservation; đại lý lữ hành cần được phản hồi. |
| Workflow hiện tại | 1. Đọc email (2 phút) → 2. Trích ngày/số phòng/loại phòng (4 phút) → 3. Kiểm tra thiếu/mâu thuẫn (2 phút) → 4. Nhập phiếu yêu cầu (2 phút) → 5. Soạn thư hỏi lại (2 phút). |
| Bottleneck | Bước 2–3 chiếm 6/12 phút; nhiều cách ghi ngày và số khách dễ gây nhập nhầm. |
| AI Solution | LLM trích xuất JSON kèm đoạn bằng chứng; rule kiểm tra ngày trả > ngày nhận, số phòng dương; nhân viên đối chiếu trước khi sử dụng. |
| Metric có số | Mục tiêu median 12 → ≤ 6 phút; exact-match ngày/số phòng ≥ 95% trên 100 email; 100% trường thiếu được để null hoặc chuyển xác nhận. |
| Dữ liệu / ranh giới | Email giả lập/đã ẩn danh; không bịa giá, quỹ phòng, chính sách hoặc tự xác nhận booking. |
| Quick Architecture | LLM Feature + Rule validation; không cần agent đặt phòng. |
| Cần kiểm chứng | Khả năng chuẩn hóa email, các ngoại lệ booking, quyền truy cập nguồn quỹ phòng nếu mở rộng. |

## Lựa chọn để phân tích sâu

Chọn **Card 1 — Xanh SM** cho bài nộp cá nhân vì có ranh giới cụ thể trong starter code, dễ kiểm thử ngưỡng pin và prompt injection bằng dữ liệu giả lập. Đây là lựa chọn phục vụ kiểm chứng kỹ thuật trong lab, chưa phải kết luận có ROI cao nhất. Card 2 và Card 3 phù hợp để khảo sát tiếp nhưng cần bộ nhãn và biểu mẫu nghiệp vụ trước khi đánh giá chất lượng. Chưa có biên bản họp nhóm; không ghi nhận giả một quyết định tập thể.

Phản biện lựa chọn: nếu chỉ xét ba action theo mức pin thì rule và mẫu câu cố định đã đủ. LLM chỉ đáng giữ khi chứng minh hỗ trợ đọc/tóm tắt ngôn ngữ tự do tốt hơn phương án đó, với thời gian duyệt và tỷ lệ sửa nháp được đo thực tế.
