import os
import subprocess

def convert_epub_to_pdf(epub_path, pdf_path):
    # 检查epub文件是否存在
    if not os.path.exists(epub_path):
        raise FileNotFoundError(f"The file {epub_path} does not exist.")

    # 使用ebook-convert进行转换.
    try:
        result = subprocess.run(
            [r'Calibre文档下的ebook-convert.exe（一定要输入完整路径）', epub_path, pdf_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
            encoding='utf-8'
        )
        print("成功转换!!!")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e.stderr}")
#测试
epub_file = r'要转换的xxx.epub文档（完整路径）'
pdf_file = r'创建一个pdf文档（同样输入完整路径）'
convert_epub_to_pdf(epub_file, pdf_file)
