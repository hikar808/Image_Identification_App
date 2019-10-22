from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

# パラメーター
classes = ['landscape', 'painting']
num_classes = len(classes)
image_size = 224

# 格納先リスト
X = [] 
Y = [] 

for index, classlabel in enumerate(classes):
    photos_dir = "./Data/" + classlabel

    # 画像フォルダ内jpgファイルの取得
    files = glob.glob(photos_dir + "/*.jpg")

    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size,image_size))
        data = np.asarray(image) 
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

# 学習用データとテスト用データに分割
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)

# データを保存
np.save("../Data/imagefiles_224.npy", xy)