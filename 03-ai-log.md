# AI Log — Nhật ký hỗ trợ làm bài

Ngày: 12/09/2026. Công cụ hỗ trợ: Codex. Đây là nhật ký những thao tác thực tế trong phiên hỗ trợ, **không phải lời tự thuật do sinh viên tự viết**. Sinh viên cần đọc, sửa và bổ sung phần phản ánh cá nhân trước khi nộp.

## Yêu cầu ban đầu

Người dùng hỏi cách làm bài trong repo và đề nghị có thể làm giúp luôn. Codex đọc README, worksheet, starter code, ví dụ và autograder; chọn scope Xanh SM phù hợp đề.

## AI đã giúp gì?

1. Chuyển rubric thành các deliverable: 5 vấn đề, 3 cards, workflow, problem statement 6-field, AI fit, evaluate, prototype và nhật ký.
2. Phân biệt rule cho ngưỡng pin với LLM để soạn nháp; không thêm agent có quyền điều xe.
3. Viết code gọi SDK, JSON schema, 4 adversarial tests, 3 controls và 12 kiểm thử offline.
4. Vẽ sơ đồ PNG và xem lại hình để kiểm tra bố cục, chữ, handoff và bottleneck.

## Sai sót, giới hạn và cách điều chỉnh thực tế

| Quan sát | Điều chỉnh | Bài học |
|---|---|---|
| Lần đọc bổ sung ban đầu dùng nhầm thư mục làm việc nên không tìm thấy file | Chỉ định đúng workdir của repo trong lệnh sau | Lỗi công cụ không đồng nghĩa file bị thiếu |
| Bản vá đầu tiên gộp xóa và tạo cùng file bị công cụ từ chối | Tách thao tác và kiểm tra file sau khi tạo | Cần kiểm tra kết quả thao tác, không chỉ dự định |
| Dữ liệu nghiệp vụ trong bài chỉ là giả định | Gắn nhãn giả định, thêm cách lấy baseline | Không biến số AI đề xuất thành dữ liệu khảo sát |
| Quy tắc thẻ draft và JSON dễ bị hiểu mâu thuẫn | Đặt thẻ ở đầu draft_message, giữ vỏ JSON hợp lệ | Định nghĩa rõ output nào dành cho hiển thị |
| Prompt đơn thuần và kiểm tra từ khóa chưa đủ | Kiểm tra trường JSON, hành động, tiền tố, duyệt và dữ liệu trạm; giữ raw output | Không sửa output rồi báo mô hình đã đạt |
| Sandbox chặn tải thư viện và kết nối API | Xin quyền mạng theo cơ chế công cụ rồi chạy lại | Tách lỗi môi trường khỏi lỗi mô hình |
| Gemini 2.5 Flash trả 404: không còn khả dụng cho người dùng mới theo phản hồi API | Giữ mặc định theo đề, thêm --model và lưu thử nghiệm model thay thế riêng | Không âm thầm đổi model rồi báo đã làm đúng yêu cầu |

Trong phiên này chưa quan sát được hallucination nghiệp vụ từ Gemini 2.5 vì không nhận được output mô hình. Các câu ép bịa ETA/trạm là **test được thiết kế**, không phải bằng chứng mô hình đã thực sự bịa.

## Bằng chứng kiểm thử

- `pytest starter-code/test_prompt_prototype.py -q`: 12 passed; chứng minh validator/fallback theo các ca đã viết, không chứng minh chất lượng Gemini.
- `prototype-results.json`: 7 lần thử model theo đề thất bại ở ClientError; chẩn đoán thêm xác định HTTP 404 NOT_FOUND.
- Nội dung thông báo 404 đã đọc: model 2.5 không còn khả dụng cho người dùng mới; API gợi ý `gemini-3.6-flash`. Không ghi API key vào báo cáo.
- `prototype-results-alternative.json`: model `gemini-3.6-flash`, 6/7 ca đạt lần đầu; ca critical_battery bị HTTP 503 ServerError, không có output. `prototype-results-retry.json`: chỉ chạy lại ca đó, đạt. Như vậy 7 tình huống có output đạt sau một lần retry; không phải 7/7 đạt trong cùng một lần chạy.
- Codex đọc 7 output thành công: đều có thẻ draft, yêu cầu duyệt, không cam kết ETA hoặc báo đã thực thi điều xe. Đây là review trên mẫu nhỏ, không chứng minh an toàn tổng quát.
- Autograder `--section-a`: 4/4 file có mặt, 5/5 điểm kiểm tra tồn tại; không phải điểm nội dung từ giảng viên.

## Phần sinh viên cần tự bổ sung

- Tôi đã tự đọc/chạy/chỉnh phần nào? [Điền sau khi thực hiện.]
- Tôi đồng ý hay không đồng ý với lựa chọn bài toán và tại sao? [Ý kiến cá nhân.]
- Một ví dụ tôi tự thay prompt và kết quả trước/sau? [Không bịa nếu chưa thử.]
- Tôi giải thích được vì sao dùng Rule + LLM thay vì Agent như thế nào? [Viết bằng lời của mình.]

Không ghi đã phỏng vấn, họp nhóm hay chạy thành công model theo đề nếu chưa có bằng chứng.
