# 簡易ツールのインストール方法

## 前提条件
Gitがインストールされていることを確認してください。
Gitがインストールされていない場合は、[Gitの公式サイト](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)からダウンロードしてインストールできます。

## リポジトリのクローン
作業ディレクトリに本リポジトリをクローンします。
例えば、デスクトップに新しいフォルダを作成してそこにクローンする場合は以下のようにします：

```
mkdir -p ~/Desktop/MyProject
cd ~/Desktop/MyProject
git clone https://github.com/tomokinakamura1/genai-excel-editor.git
```

## 依存関係のインストール

Python 3.11 を使用していることを確認してください。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 環境変数の準備

一時的な環境ファイルをコピーして名前を変更します：

```bash
cp .env_temp .env
```
`.env` ファイルに PROJECT_ID、IBM_CLOUD_URL と IBM_CLOUD_API_KEY を追加してください。

## 実行方法

プロジェクトディレクトリで以下を実行できます：

```bash
python gradio-ui_jp.py
```
ブラウザで [http://localhost:8080](http://localhost:8080) を開いて表示します。

