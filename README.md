# 山手線E235系の側面行先表示器の画像と画像作成器のリポジトリ
![yamanote_line](images/generated//uchimawari/003.png)
&nbsp;
![uchi_next_akihabara_ja](images/generated//uchimawari/004.png)
&nbsp;
![uchi_next_akihabara_en](images/generated//uchimawari/005.png)

上記の行先表示器の画像自体と、それをテンプレート画像から作成するためのスクリプトのリポジトリです。


## 画像の仕様について
このリポジトリの画像はLEDマトリクスを使って実際に点灯させることを前提としています。

画像サイズは32 x 128となっており、LEDマトリクスの光り方に合わせてグラデーションはかなり濃く表現しています。

そのため、PC上で画像を表示させた場合は実車のイメージとは少々異なりますが、LEDマトリクス上で表示した場合は実車のイメージにできる限り近くなるようにしています。

また、このリポジトリの画像は自身で撮影した写真をもとに作成しているため、実車とは異なる可能性があることはご了承ください。


## 作成済みの画像
`images/generated`ディレクトリ下に内回り分、外回り分の作成済みの画像も置いてあります。この画像をそのまま使用するのであれば下の画像作成は必要ありません。


## 画像作成器の使用方法
以下のようなテンプレート画像を組み合わせて上記の作成済み画像を作成するPythonスクリプトを用意しています。これらの素材画像はすべて`images/materials`ディレクトリにあります。

![background](images/materials/background.png)
&nbsp; 背景

![base_text_ja](images/materials/base_text_ja.png)
&nbsp; 日本語表記テンプレート

![uchimawari_01_ueno_ikebukuro](images/materials/uchi_01_ueno_ikebukuro_ja.png)
&nbsp; 方面

![akihabara_ja](images/materials/03_akihabara_ja.png)
&nbsp; 次の駅名



以下のコマンドでPythonスクリプトを実行すると`images/generated`下に画像が作成されます。
その際、`images/generated`内に**もともとあったファイルはすべて削除される**ので注意してください。
また、スクリプト内でPILライブラリを使用しているので、インストールされていない場合はインストールしてから以下コマンドを実行してください。

```bash
python generate_yamanote_e235_images.py
```


## 画像・コードの使用に関して
- imagesフォルダ内のすべての画像について
  - 良識の範囲内で自由に楽しんで使ってください！
  - imagesフォルダ内の画像を使用することによって生じたいかなる問題についても作者は責任を負いません。
- コード部分に関しては[MITライセンス](LICENSE)です。


