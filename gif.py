from PIL import Image, ImageDraw

# 画像のパス
image_path = ''

# 元の画像を読み込む
base_image = Image.open(image_path)
base_image = base_image.convert("RGBA")  # RGBAに変換して透明度をサポート

# フレームを保存するリスト
frames = []

# キャンバスのサイズを設定
canvas_size = (1700, 3000)  # 必要に応じて変更
num_frames = 60  # フレーム数

# 画像を20度と-20度で交互に回転させながらパラパラアニメを作成
for i in range(num_frames):
    # 新しいフレームを作成
    frame = Image.new('RGBA', canvas_size, (255, 255, 255, 128))  # 白い背景

    # 画像の位置を計算
    x = (canvas_size[0] - base_image.width) // 2
    y = (canvas_size[1] - base_image.height) // 2

    # 20度と-20度で交互に回転させる
    angle = 20 if i % 2 == 0 else -20
    rotated_image = base_image.rotate(angle, resample=Image.BICUBIC, expand=True)
    frame.paste(rotated_image, (x, y), rotated_image)
    
    
    #  # 角度を計算
    # angle = 20 - (i / (num_frames - 1)) * 40  # 20度から-20度に変化
    
    # # 画像を回転してフレームに貼り付け
    # rotated_image = base_image.rotate(angle, resample=Image.BICUBIC, expand=True)
    # frame.paste(rotated_image, (x, y), rotated_image)

    # フレームをリストに追加
    frames.append(frame)

# GIFを保存
frames[0].save('rotating_image_animation.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)
