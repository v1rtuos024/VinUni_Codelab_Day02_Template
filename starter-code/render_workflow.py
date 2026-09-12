"""Render the assumed current workflow using Pillow and Windows fonts."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
image = Image.new("RGB", (1800, 1040), "#f5f7fb")
draw = ImageDraw.Draw(image)


def font(size, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("arialbd.ttf" if bold else "arial.ttf"), size)


def text(x, y, value, size=24, color="#243349", bold=False):
    draw.text((x, y), value, font=font(size, bold), fill=color, spacing=12)


text(70, 55, "XANH SM | QUY TRÌNH HIỆN TẠI", 43, bold=True)
text(70, 120, "Mô hình giả định cho bài lab — chưa xác minh với đơn vị vận hành", 26)
text(70, 175, "15 phút/lượt = 2 + 2 + 5 + 4 + 2 phút xử lý chủ động", 30, "#165a82", True)
steps = [
    ("01  TIẾP NHẬN", "2 phút", "Tài xế → điều phối", "Điện thoại → ticket", "Ghi nhận báo pin yếu"),
    ("02  XÁC MINH", "2 phút", "Điều phối viên", "Ticket → pin / vị trí", "Đối chiếu dashboard"),
    ("03  TRA PHƯƠNG ÁN", "5 phút", "Điều phối viên", "Dữ liệu → phương án", "Tra danh bạ / bản đồ"),
    ("04  SOẠN VÀ DUYỆT", "4 phút", "Điều phối viên", "Phương án → nháp duyệt", "Viết và kiểm tra tin"),
    ("05  LIÊN HỆ", "2 phút", "Điều phối → bên nhận", "Tin duyệt → log liên hệ", "Tài xế / đội hỗ trợ"),
]
for i, step in enumerate(steps):
    x = 70 + i * 335
    bottleneck = i in (2, 3)
    draw.rounded_rectangle((x, 295, x + 310, 600), 16, fill="#fff0eb" if bottleneck else "white",
                           outline="#bd4f32" if bottleneck else "#becbdc", width=3)
    text(x + 16, 320, step[0], 21, bold=True)
    text(x + 16, 365, step[1], 36, "#ac3e24" if bottleneck else "#165a82", True)
    for row, label in enumerate(step[2:]):
        text(x + 16, 435 + 43 * row, label, 21)
    if bottleneck:
        text(x + 16, 560, "BOTTLENECK", 20, "#ac3e24", True)
    if i < 4:
        draw.line((x + 312, 410, x + 332, 410), fill="#506580", width=3)
        draw.polygon([(x + 332, 410), (x + 323, 404), (x + 323, 416)], fill="#506580")
text(70, 660, "CÁC ĐIỂM BÀN GIAO (HANDOFF)", 26, bold=True)
text(70, 710, "H1  Tài xế → điều phối: báo cáo thành ticket\nH2  Điều phối ↔ dashboard xe: xác minh nguồn pin và vị trí\nH3  Điều phối → tài xế / đội hỗ trợ: chuyển nội dung đã duyệt", 26)
text(70, 865, "Ngoại lệ: thiếu dữ liệu ở bước 2 → hỏi lại bước 1; phương án không khả dụng → tra lại bước 3.", 25)
text(70, 920, "Chưa tính thời gian chờ, hỏi lại và thời gian hỗ trợ đến nơi. Không phải số liệu thực tế của Xanh SM.", 24)
image.save(ROOT / "04-workflow-diagram.png")
