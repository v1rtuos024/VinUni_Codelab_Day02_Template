# Reproducible code-drawn PNG for the current-state workflow (no image model).
Add-Type -AssemblyName System.Drawing
$taskRoot = Split-Path $PSScriptRoot -Parent
$bmp = [System.Drawing.Bitmap]::new(1800, 1150)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$g.Clear([System.Drawing.Color]::FromArgb(246,248,252))
$dark = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(24,40,64))
$muted = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(76,91,112))
$blue = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(35,92,160))
$red = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(180,45,53))
$title = [System.Drawing.Font]::new('Segoe UI',32,[System.Drawing.FontStyle]::Bold)
$heading = [System.Drawing.Font]::new('Segoe UI',23,[System.Drawing.FontStyle]::Bold)
$body = [System.Drawing.Font]::new('Segoe UI',20)
$small = [System.Drawing.Font]::new('Segoe UI',17)
$g.DrawString('XANH SM | QUY TRÌNH HIỆN TẠI', $title, $dark, 70, 40)
$g.DrawString('Xử lý báo cáo sự cố pin • Bài nộp v1rtuos024 • Mô phỏng trong lab', $body, $muted, 74, 105)
$g.DrawString('Thời gian là giả định; chưa khảo sát hoặc đo logs vận hành thực tế.', $small, $red, 74, 152)
$steps = @(
    @('01  Tiếp nhận báo cáo','Tài xế → Điều phối viên','Cuộc gọi / tin nhắn → ticket','2 phút', $false),
    @('02  Xác minh thông tin','Điều phối viên ↔ nguồn dữ liệu / tài xế','Kiểm tra mức pin và vị trí','2 phút', $false),
    @('03  Tra cứu phương án','Điều phối viên ↔ đầu mối hỗ trợ','Kiểm tra phương án và khả dụng','5 phút • BOTTLENECK', $true),
    @('04  Soạn và rà soát','Điều phối viên','Viết nháp, đối chiếu, duyệt nội dung','5 phút • BOTTLENECK', $true),
    @('05  Gửi / chuyển và ghi log','Điều phối viên → tài xế / đội hỗ trợ','Phản hồi đã duyệt → mã yêu cầu','1 phút', $false)
)
$pen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(35,92,160),4)
$pen.EndCap = [System.Drawing.Drawing2D.LineCap]::ArrowAnchor
for ($i=0; $i -lt $steps.Count; $i++) {
    $y=220+$i*155
    $fill = if ($steps[$i][4]) { [System.Drawing.Color]::FromArgb(255,236,236) } else { [System.Drawing.Color]::White }
    $brush=[System.Drawing.SolidBrush]::new($fill)
    $g.FillRectangle($brush,350,$y,1320,130)
    $g.DrawString($steps[$i][0],$heading,$dark,375,($y+12))
    $g.DrawString($steps[$i][1],$small,$blue,375,($y+55))
    $g.DrawString($steps[$i][2],$small,$muted,375,($y+89))
    $timeBrush=if ($steps[$i][4]) {$red} else {$blue}
    $g.DrawString($steps[$i][3],$body,$timeBrush,1260,($y+35))
    if ($i -lt 4) { $g.DrawLine($pen,1000,($y+132),1000,($y+153)) }
    $brush.Dispose()
}
$g.DrawString('H1 • Bàn giao', $heading,$blue,70,240)
$g.DrawString('Tài xế → điều phối', $small,$muted,70,290)
$g.DrawString('H2 • Xác minh', $heading,$blue,70,397)
$g.DrawString("Thiếu dữ liệu:`nquay lại bước 01", $small,$muted,70,448)
$g.DrawString('10 / 15 phút', $heading,$red,70,560)
$g.DrawString("Tra cứu + soạn tin`nchiếm 66,7%", $small,$muted,70,609)
$g.DrawString('H3 • Bàn giao', $heading,$blue,70,858)
$g.DrawString("Gửi tài xế /`nchuyển đội hỗ trợ", $small,$muted,70,904)
$g.DrawString('TỔNG: 15 PHÚT / LƯỢT', $heading,$dark,70,1020)
$g.DrawString('2 + 2 + 5 + 5 + 1 • Chưa tính chờ bổ sung thông tin, di chuyển cứu hộ hoặc sửa chữa.', $small,$muted,70,1070)
$bmp.Save((Join-Path $taskRoot '04-workflow-diagram.png'),[System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()
