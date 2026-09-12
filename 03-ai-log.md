## Nhật ký tương tác AI (AI Log & Reflection)

**Người thực hiện:** [Tên của bạn]
**Bài toán lựa chọn:** Trợ lý hướng dẫn trạm sạc thông minh VinFast

Trong suốt quá trình thực hiện Lab 02 (AI Product Scoping cho Vin Smart Future), tôi đã sử dụng mô hình LLM (Gemini) làm "Thought-Partner" (trợ lý tư duy) để hỗ trợ quá trình brainstorm, phân tích chuyên sâu và stress-test ý tưởng. Dưới đây là những phản ánh chân thực về quá trình tương tác này.

---

### 1. AI đã giúp tôi những gì?

*   **Tăng tốc độ Brainstorm (Phase 1):** Ban đầu, việc tìm ra 5 bài toán thực tế cho nhiều mảng kinh doanh của Vingroup khá mất thời gian. Khi tôi sử dụng prompt *"Tôi là AI Engineer tại Vin Smart Future... Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công..."*, AI đã cung cấp ngay các ý tưởng rất sát với thực tế vận hành (ví dụ: lỗi trạm sạc, phân loại review, điều vận taxi). Điều này giúp tôi vượt qua sự bế tắc ban đầu và chọn được bài toán "Trạm sạc thông minh VinFast" một cách nhanh chóng.
*   **Hoàn thiện cấu trúc Problem Statement (Phase 3):** AI hỗ trợ rất tốt trong việc cấu trúc hóa suy nghĩ. Khi tôi cung cấp các ý tưởng thô về nỗi đau của tài xế xe điện, AI đã giúp tôi sắp xếp gọn gàng vào framework 6-field (Actor, Current Workflow, Bottleneck, Business Impact, Metric, Boundary), giúp báo cáo trở nên chuyên nghiệp và đáp ứng đúng tiêu chuẩn đánh giá của Lab.
*   **Vẽ sơ đồ luồng (Phase 4):** Việc dùng AI (đặc biệt là syntax Mermaid) để trực quan hóa quy trình hiện tại và tương lai giúp tôi tiết kiệm nhiều thời gian so với việc phải vẽ thủ công trên các phần mềm đồ họa.

---

### 2. AI đã trả lời sai / Hallucination ở đâu?

Dù rất hữu ích, AI vẫn mắc phải một số sai lầm (hallucinations) khi phân tích sâu vào nghiệp vụ đặc thù của VinFast:
*   **Sai lệch về kiến thức phần cứng:** Trong lần prompt đầu tiên, AI đã đề xuất tự động điều hướng xe đến một trạm sạc có cổng "CHAdeMO". Trên thực tế, xe VinFast phân phối tại Việt Nam và toàn cầu chủ yếu dùng chuẩn CCS2, hoặc chuẩn GBT (cho một số dòng xe chuyên biệt). Đề xuất này là một hallucination về kiến thức kỹ thuật ô tô, hoàn toàn không khả thi để áp dụng cho Vingroup.
*   **Vượt ranh giới an toàn (Operational Boundary):** Khi tôi yêu cầu AI phác thảo luồng Future-State, AI ban đầu đã đề xuất: *"Xe tự động bẻ lái và điều hướng tài xế đến trạm sạc gần nhất ngay khi pin yếu"*. Đây là một lỗi nghiêm trọng về an toàn giao thông, vi phạm nguyên tắc "Human-in-the-loop" vì xe không được quyền tự đổi hướng mà không có sự phê duyệt (click/giọng nói) của người lái.
*   **Đề xuất số liệu Metric thiếu thực tế:** AI đề xuất "Giảm thời gian xử lý xuống 0.01 giây". Con số này nghe có vẻ "công nghệ" nhưng thiếu tính thực tế trong môi trường xe cộ (cần thời gian API phản hồi và thời gian tài xế nghe - phản hồi giọng nói).

---

### 3. Cách tôi đã sửa Prompt và Ranh giới (Boundary) để đạt kết quả chuẩn

Nhận ra những điểm mù của LLM, tôi đã tinh chỉnh lại cách đặt Prompt theo hướng áp đặt ranh giới (System Prompting) nghiêm ngặt hơn:

*   **Sửa lỗi kỹ thuật:** Tôi đã bổ sung Context (Bối cảnh) rõ ràng vào prompt: *"Bạn là một kỹ sư xe điện VinFast. Xe VinFast hiện tại chỉ hỗ trợ cổng sạc CCS2 và GBT. Tuyệt đối không đề xuất các chuẩn sạc khác."* Kết quả sau đó hoàn toàn chuẩn xác.
*   **Thiết lập Ranh giới An toàn (Boundary):** Thay vì để AI tự vẽ luồng, tôi định nghĩa rõ ranh giới trong Prompt: *"AI chỉ được phép 'Draft' (đề xuất) lộ trình. Tài xế PHẢI là người có quyền quyết định cuối cùng (Human-in-the-loop) để kích hoạt lộ trình. Tuyệt đối cấm AI tự động thay đổi lộ trình lái xe."*
*   **Điều chỉnh Metric:** Tôi prompt AI rằng: *"Hãy điều chỉnh Metric thành một con số thực tế có thể đo lường được bằng thao tác tay/giọng nói của con người trong khoang lái (ví dụ: dưới 30 giây), thay vì tốc độ xử lý của máy chủ."*

**Kết luận:**
Việc sử dụng LLM không phải là copy-paste mù quáng. LLM là một công cụ mạnh mẽ để tạo ra bộ khung ban đầu, nhưng vai trò của tôi (AI Product Engineer) là "người gác cổng" (Gatekeeper) — người hiểu rõ bối cảnh kinh doanh, thiết lập các ranh giới an toàn (boundaries) và tinh chỉnh đầu ra để AI phục vụ đúng mục tiêu kinh doanh thực tế.