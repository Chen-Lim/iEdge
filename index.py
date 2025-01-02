import os
import subprocess


def list_models(models_folder):
    """列出 models 文件夹下所有支持的型号脚本"""
    model_files = [f for f in os.listdir(models_folder) if f.endswith('.py')]
    models = {idx + 1: f[:-3] for idx, f in enumerate(model_files)}  # 创建编号和型号映射
    return models


def main():
    """主程序，提供用户选择界面并运行对应脚本"""
    models_folder = './models'  # 存放型号脚本的文件夹
    masks_folder = './masks'  # 存放边框图片的文件夹

    print("欢迎使用 iEdge ！")

    # 检查文件夹是否存在
    if not os.path.exists(models_folder):
        print(f"错误：未找到 {models_folder} 文件夹，请检查文件结构。")
        return
    if not os.path.exists(masks_folder):
        print(f"错误：未找到 {masks_folder} 文件夹，请检查文件结构。")
        return

    print("以下是支持的产品型号：")
    models = list_models(models_folder)
    if not models:
        print("没有找到任何型号处理程序，请确认 models 文件夹下的脚本是否存在！")
        return

    # 列出型号
    for idx, model in models.items():
        print(f"{idx}. {model}")

    try:
        choice = int(input("请输入要处理的型号编号："))
        if choice not in models:
            print("无效的选择，请重新运行程序。")
            return

        # 获取选择的脚本路径
        model_script = os.path.join(models_folder, models[choice] + '.py')
        print(f"正在运行 {model_script}...")
        subprocess.run(['python', model_script])  # 调用对应型号的脚本
    except ValueError:
        print("输入无效，请输入一个数字。")
    except Exception as e:
        print(f"运行时发生错误：{e}")


if __name__ == "__main__":
    main()
