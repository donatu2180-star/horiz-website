# デプロイ手順

このサイトを Cloudflare Pages にデプロイし、`horiz-ai.com` ドメインで公開する手順。

## 必要なもの

- GitHub アカウント（無料）
- Cloudflare アカウント（無料、サインアップ）
- Hostinger アカウント（既存。DNS A レコード変更のみ。メール継続用）

**追加課金: なし**（GitHub・Cloudflare Pages・Cloudflare DNS は全て無料枠で動く）

---

## Step 1: GitHub リポジトリを作る

### 1-1. GitHub で新規リポジトリ作成
1. https://github.com/new にアクセス
2. Repository name: `horiz-website`
3. Public/Private: どちらでも可（推奨: Private）
4. その他オプションは何もチェックせず「Create repository」

### 1-2. ローカルから push
このディレクトリ内で：

```bash
git remote add origin https://github.com/YOUR-USERNAME/horiz-website.git
git branch -M main
git push -u origin main
```

認証で Personal Access Token を求められたら：
- GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic)
- スコープ: `repo` を選択
- 生成されたトークンをパスワード欄に貼り付け

---

## Step 2: Cloudflare Pages に接続

### 2-1. Cloudflare 登録
1. https://dash.cloudflare.com/sign-up にサインアップ（既存アカウントあればスキップ）

### 2-2. Cloudflare Pages プロジェクト作成
1. Cloudflare ダッシュボード → Workers & Pages → Create → Pages → Connect to Git
2. 「Connect GitHub」を選択し、horizの GitHub アカウントを連携
3. リポジトリ `horiz-website` を選択

### 2-3. ビルド設定
- Project name: `horiz-website`
- Production branch: `main`
- Framework preset: **None**
- Build command: 空欄でOK
- Build output directory: `/`（ルート）

「Save and Deploy」を押す → 数十秒でビルド完了
プレビューURL: `https://horiz-website.pages.dev` が発行される

---

## Step 3: プレビューで確認

`https://horiz-website.pages.dev` をブラウザで開き、全ページの動作確認：
- [ ] トップ
- [ ] 会社概要
- [ ] 企業研修
- [ ] AI/DXコンサル
- [ ] システム開発
- [ ] お知らせ
- [ ] FAQ
- [ ] お問い合わせ
- [ ] スマホでも崩れない（実機チェック推奨）

---

## Step 4: 独自ドメインを接続

### 4-1. Cloudflare Pages 側
1. Cloudflare Pages → horiz-website → Custom domains → Set up a custom domain
2. ドメイン入力: `horiz-ai.com`
3. 「Continue」→ 表示される DNS 設定を確認

### 4-2. Hostinger DNS 側（重要）

**現状**: `horiz-ai.com` のドメイン管理は Hostinger。
A レコードが Hostinger サーバを指している。

**変更**:
1. Hostinger ログイン → Domains → `horiz-ai.com` → DNS / Nameservers
2. **A レコード**を編集：
   - 旧値（Hostingerサーバ）→ 削除
   - 新値: Cloudflare Pages が指示する CNAME (`horiz-website.pages.dev`) を `@` (ルート) に CNAME として追加
3. **MX レコード**: そのまま維持（メール用、変更しない）
4. **CNAME (www)**: `horiz-ai.com` を指すよう設定

⚠️ **DNS 反映には数分〜最大48時間かかる可能性あり**（通常は5-30分）

### 4-3. 確認
- 数分待つ
- `horiz-ai.com` をブラウザで開く → Cloudflare Pages の内容が表示されれば成功
- `ryuki.izumi@horiz-ai.com` 宛のテストメールが届く → メール継続OK

---

## トラブルシューティング

### サイトが表示されない
- DNS 反映待ち（最大48時間）
- ブラウザキャッシュをクリア
- Cloudflare Pages のデプロイが「Success」状態か確認

### メールが届かなくなった
- MX レコードを誤って削除した可能性
- Hostinger ヘルプ → MX レコードを再設定: `mx1.hostinger.com` (priority 5), `mx2.hostinger.com` (priority 10)

### CSS が反映されない
- ブラウザのスーパーリロード（`Cmd+Shift+R`）
- Cloudflare Pages のキャッシュをパージ: ダッシュボード → Caching → Purge Everything

---

## ロールバック方法

問題が起きたら DNS を元に戻すだけで Hostinger の旧サイトに戻る。
1. Hostinger DNS で A レコードを Hostinger 旧サーバに戻す
2. CNAME を削除
3. 数分で旧サイト復旧

GitHub のコミット履歴で全変更が追跡できるので、コード自体のロールバックは `git revert` で可能。
