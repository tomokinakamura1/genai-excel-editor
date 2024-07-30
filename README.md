# ISUZU Spss

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

