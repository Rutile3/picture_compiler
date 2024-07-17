import os
from PIL import Image


# mainの関数
def main_func():
    folder_in_img = "02_folder_in_img"
    folder_out_pdf = "03_pdf"

    # 出力フォルダーが存在しない場合は作成
    if not os.path.exists(folder_out_pdf):
        os.makedirs(folder_out_pdf)

    convert_images_to_pdf(folder_in_img, folder_out_pdf)

    input("enterキーでプログラムを終了します。")


# 画像をPDFに変換
def convert_images_to_pdf(folder_in_img, folder_out_pdf):
    # 各フォルダーのパスを取得
    for subdir, dirs, files in os.walk(folder_in_img):
        if subdir == folder_in_img:
            continue
        # フォルダー名を取得
        folder_name = os.path.basename(subdir)
        # 出力先のPDFファイル名を決定
        pdf_path = os.path.join(folder_out_pdf, f"{folder_name}.pdf")

        # 画像ファイルを収集
        images = []
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                file_path = os.path.join(subdir, file)
                img = Image.open(file_path).convert("RGB")
                images.append(img)

        # 画像が存在する場合、PDFを作成
        if images:
            images[0].save(pdf_path, save_all=True, append_images=images[1:])


# mainの関数呼び出し
if __name__ == "__main__":
    main_func()
