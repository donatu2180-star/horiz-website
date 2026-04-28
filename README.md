# horiz-ai.com — 静的サイト

株式会社horizの公式サイト。Cloudflare Pages にホスティング、ドメイン `horiz-ai.com`。

## 構成

```
.
├── index.html              # トップページ
├── about/                  # 会社概要
├── training/               # 企業研修
├── consulting/             # AI/DXコンサルティング
├── development/            # AIシステム開発
├── news/                   # お知らせ
├── faq/                    # FAQ
├── contact/                # お問い合わせ
├── assets/
│   ├── css/style.css       # 全体スタイル
│   └── images/             # ロゴ、サービス画像、コース画像、事例画像など
└── build.py                # ページ生成スクリプト（コンテンツ変更時に実行）
```

## ローカルプレビュー

```bash
cd /path/to/this-repo
python3 -m http.server 8910
# → http://localhost:8910/ で確認
```

## コンテンツを変更する

### 1. テキスト変更
`build.py` の `home_main` / `training_main` / `consulting_main` などの該当箇所を編集 → `python3 build.py` 実行。

### 2. 画像変更
`assets/images/` 配下のファイルを置き換え。ファイル名は維持。

### 3. 新ページ追加
`build.py` の `PAGES` 配列に追加 → 実行。

### 4. デザイン変更
`assets/css/style.css` を編集（HTMLは触らずに済む構造）。

## デプロイ

GitHub に push すれば Cloudflare Pages が自動でビルド＆公開する。

```bash
git add .
git commit -m "コンテンツ更新"
git push origin main
```

数十秒で `https://horiz-ai.com` に反映される。

## ドメイン設定

- **horiz-ai.com**: Cloudflare DNS が管理。A レコードは Cloudflare Pages を指す
- **メール**: Hostinger SMTP (`smtp.hostinger.com:587`) 継続使用。MX レコードはそのまま

## デザインシステム

### カラー
- 背景: `#131D32` (dark navy)
- メインテキスト: `#F5F0E8` (cream)
- アクセント teal: `#26A69A`
- アクセント gold: `#D4A862`

### フォント
- 見出し: Shippori Mincho (明朝)
- 本文: Noto Sans JP / Inter (英数)

### 主要コンポーネント
- ヒーロー（写真+テキスト2カラム）
- USP 3カラム（番号付きエディトリアル）
- DX推進フロー（明朝＋teal左罫線）
- 北大認定テスティモニアル
- サービスタイル（画像+テキスト）
- 補助金チップ（gold枠）
- FAQ アコーディオン

## メンテナンス連絡先

技術担当: 泉龍希 (`ryuki.izumi@horiz-ai.com`)
