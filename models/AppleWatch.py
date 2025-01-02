from PIL import Image, ImageDraw
import os

def create_rounded_image_with_border(image_path, mask_path, output_path):

    # 定义画布和遮罩尺寸
    canvas_size = (540, 880)
    rounded_size = (396, 484)
    radius = 10

    # 创建画布
    canvas = Image.new('RGBA', canvas_size, (0, 0, 0, 0))

    # 打开原始图片并调整大小以适应圆角区域
    img = Image.open(image_path).convert("RGBA")
    img = img.resize(rounded_size, Image.LANCZOS)

    # 创建圆角遮罩
    mask = Image.new('L', rounded_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, rounded_size[0], rounded_size[1]), radius=radius, fill=255)

    # 应用遮罩以创建圆角图片
    rounded_img = Image.new('RGBA', rounded_size)
    rounded_img.paste(img, (0, 0), mask)

    # 将圆角图片粘贴到画布中央
    x_offset = (canvas_size[0] - rounded_size[0]) // 2
    y_offset = (canvas_size[1] - rounded_size[1]) // 2
    canvas.paste(rounded_img, (x_offset, y_offset))

    # 打开边框图片并覆盖到画布
    border = Image.open(mask_path).convert("RGBA")
    canvas.paste(border, (0, 0), border)

    # 保存结果
    canvas.save(output_path, "PNG")

if __name__ == "__main__":
    # 输入图片文件夹和输出文件夹
    input_folder = "./images"
    output_folder = "./images_output"
    mask_path = "./masks/AppleWatch.png"

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 支持的文件格式
    supported_formats = (".png", ".jpg", ".jpeg", ".bmp")

    # 扫描输入文件夹中的所有图片
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_formats)]
    print(f"发现 {len(image_files)} 张图片正在处理...")

    for image_name in image_files:
        input_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, image_name)

        try:
            create_rounded_image_with_border(input_path, mask_path, output_path)
            print(f"成功处理: {image_name}")
        except Exception as e:
            print(f"处理失败: {image_name}, 错误: {e}")

    print("全部处理完成！")
