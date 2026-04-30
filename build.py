#!/usr/bin/env python3
"""
horiz-ai.com static page generator.

目的: 現行 Hostinger 版 horiz-ai.com の見た目をほぼ完全再現する。
編集ポリシー:
  - テキストはすべて本物（source_dump 由来）。捏造禁止。
  - レイアウトは Hostinger 版に近づける（フル背景ヒーロー、シンプルな3カラム、CTA pill）。
  - assets/css/style.css を使い回す。HTML には class 名のみ。
"""

import os
import time

ROOT = os.path.dirname(os.path.abspath(__file__))

# CSS/JS ファイルのキャッシュバスター。ビルドごとに新しい値が入る。
ASSET_VERSION = str(int(time.time()))

# ────────────────────────────────────────────────────────────────────────────
# ナビゲーション
# ────────────────────────────────────────────────────────────────────────────
NAV_ITEMS = [
    ("Home",       "/"),
    ("会社概要",    "/about/"),
    ("事業内容",    None),
    ("お知らせ",    "/news/"),
    ("お問い合わせ", "/contact/"),
    ("FAQ",        "/faq/"),
]
NAV_DROPDOWN = [
    ("企業研修",            "/training/"),
    ("AI/DXコンサルティング", "/consulting/"),
    ("システム開発",         "/development/"),
]


def header(active):
    items = []
    for label, href in NAV_ITEMS:
        cls = "nav-item"
        if (href and active == href) or (label == "Home" and active == "/"):
            cls += " is-active"
        if label == "事業内容":
            sub = "".join(
                f'<a class="nav-sub-item" href="{h}">{l}</a>' for l, h in NAV_DROPDOWN
            )
            items.append(
                f'<li class="{cls} has-dropdown">'
                f'  <span class="nav-link">{label}<span class="caret">▾</span></span>'
                f'  <div class="nav-dropdown">{sub}</div>'
                f'</li>'
            )
        else:
            items.append(f'<li class="{cls}"><a class="nav-link" href="{href}">{label}</a></li>')

    return f'''
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/">
      <img src="/assets/images/logo_white.png" alt="horiz — Innovate beyond horizons" class="brand-mark">
    </a>
    <button class="nav-toggle" aria-label="メニューを開く" aria-expanded="false" aria-controls="primaryNav">
      <span></span><span></span><span></span>
    </button>
    <nav class="primary-nav" id="primaryNav">
      <ul class="nav-list">{''.join(items)}</ul>
    </nav>
  </div>
</header>'''


def footer():
    return '''
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-col footer-brand">
        <img src="/assets/images/logo_white.png" alt="horiz" class="footer-logo">
        <p class="footer-tagline">中小企業に AI の進化を届ける</p>
      </div>
      <nav class="footer-col" aria-label="フッター・ナビゲーション">
        <h4 class="footer-heading">事業内容</h4>
        <ul class="footer-links">
          <li><a href="/training/">企業研修</a></li>
          <li><a href="/consulting/">AI/DXコンサルティング</a></li>
          <li><a href="/development/">AIシステム開発</a></li>
        </ul>
      </nav>
      <nav class="footer-col" aria-label="フッター・会社情報">
        <h4 class="footer-heading">会社</h4>
        <ul class="footer-links">
          <li><a href="/about/">会社概要</a></li>
          <li><a href="/news/">お知らせ</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/contact/">お問い合わせ</a></li>
        </ul>
      </nav>
      <div class="footer-col">
        <h4 class="footer-heading">所在地</h4>
        <p class="footer-address">〒001-0012<br>北海道札幌市北区北12条西1丁目</p>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="copyright">© 2025 株式会社horiz. All rights reserved.</p>
    </div>
  </div>
</footer>'''


def scroll_progress():
    return '<div class="scroll-progress" aria-hidden="true"></div>'


SITE_URL = "https://horiz-ai.com"
OG_IMAGE = f"{SITE_URL}/assets/images/home_hero.png"


JSONLD_ORGANIZATION = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Organization", "LocalBusiness"],
  "name": "株式会社horiz",
  "alternateName": "horiz",
  "url": "https://horiz-ai.com",
  "logo": "https://horiz-ai.com/assets/images/logo_white.png",
  "image": "https://horiz-ai.com/assets/images/home_hero.png",
  "description": "AI・DX領域に特化したテクノロジー企業。札幌・北海道発、北大認定スタートアップ。法人研修、AI/DXコンサルティング、AIシステム開発の3本柱で中小企業をワンストップ支援。",
  "founder": {
    "@type": "Person",
    "name": "西浦 翼",
    "jobTitle": "代表取締役"
  },
  "foundingDate": "2025-03-10",
  "address": {
    "@type": "PostalAddress",
    "postalCode": "001-0012",
    "addressRegion": "北海道",
    "addressLocality": "札幌市北区",
    "streetAddress": "北12条西1丁目",
    "addressCountry": "JP"
  },
  "areaServed": {
    "@type": "Country",
    "name": "Japan"
  },
  "knowsAbout": ["AI", "DX", "深層学習", "画像処理", "機械学習", "生成AI"],
  "sameAs": []
}
</script>'''


JSONLD_SERVICES = {
    "/training/": '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "企業研修 (AI/DX)",
  "provider": {"@type": "Organization", "name": "株式会社horiz", "url": "https://horiz-ai.com"},
  "description": "生成AIを学んで社内DXを達成、社内で専門的なAI人材を育成、助成金で研修費最大75%OFF。札幌発、オンライン全国対応。",
  "serviceType": "AI/DX法人研修",
  "areaServed": {"@type": "Country", "name": "Japan"},
  "offers": {"@type": "Offer", "url": "https://horiz-ai.com/training/", "availability": "https://schema.org/InStock"}
}
</script>''',
    "/consulting/": '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "AI/DXコンサルティング",
  "provider": {"@type": "Organization", "name": "株式会社horiz", "url": "https://horiz-ai.com"},
  "description": "社内のDXを進め業務効率化、AI導入で課題解決、助成金で低コストに実現。IT導入補助金・ものづくり補助金の活用支援。",
  "serviceType": "AI/DXコンサルティング",
  "areaServed": {"@type": "Country", "name": "Japan"},
  "offers": {"@type": "Offer", "url": "https://horiz-ai.com/consulting/", "availability": "https://schema.org/InStock"}
}
</script>''',
    "/development/": '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "AIシステム開発",
  "provider": {"@type": "Organization", "name": "株式会社horiz", "url": "https://horiz-ai.com"},
  "description": "自社独自のAIシステムを開発。画像処理や時系列データなど高い専門性。PoCから運用までワンストップで支援。",
  "serviceType": "AIシステム開発",
  "areaServed": {"@type": "Country", "name": "Japan"},
  "offers": {"@type": "Offer", "url": "https://horiz-ai.com/development/", "availability": "https://schema.org/InStock"}
}
</script>''',
}


SITE_JS = '''<script>
(function () {
  // ────── 旧Hostinger版のService Worker / Cache Storage を一括解除 ──────
  // Hostinger Builder製のサイトはPWA化のためSWを登録していたため、
  // URLバー直打ちで古いキャッシュが返る問題が発生する。これを掃除する。
  if ('serviceWorker' in navigator && navigator.serviceWorker.getRegistrations) {
    navigator.serviceWorker.getRegistrations().then(function (regs) {
      regs.forEach(function (r) { try { r.unregister(); } catch (e) {} });
    }).catch(function () {});
  }
  if (typeof caches !== 'undefined' && caches.keys) {
    caches.keys().then(function (keys) {
      keys.forEach(function (k) { try { caches.delete(k); } catch (e) {} });
    }).catch(function () {});
  }

  // ────── ヘッダー / Back-to-Top / Floating CTA / スクロール進捗バー ──────
  var header = document.querySelector('.site-header');
  var backTop = document.querySelector('.back-to-top');
  var floatCta = document.querySelector('.floating-cta');
  var progress = document.querySelector('.scroll-progress');
  var lastScroll = -1;
  var rafId = null;
  function updateScrollUI() {
    rafId = null;
    var y = window.pageYOffset || document.documentElement.scrollTop;
    if (y === lastScroll) return;
    lastScroll = y;
    if (header) {
      if (y > 40) header.classList.add('is-scrolled');
      else header.classList.remove('is-scrolled');
    }
    if (backTop) {
      if (y > 600) backTop.classList.add('is-visible');
      else backTop.classList.remove('is-visible');
    }
    if (floatCta) {
      if (y > 400) floatCta.classList.add('is-visible');
      else floatCta.classList.remove('is-visible');
    }
    if (progress) {
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docH > 0 ? Math.min(100, (y / docH) * 100) : 0;
      progress.style.transform = 'scaleX(' + (pct / 100) + ')';
    }
  }
  window.addEventListener('scroll', function () {
    if (rafId === null) rafId = window.requestAnimationFrame(updateScrollUI);
  }, { passive: true });
  updateScrollUI();
  if (backTop) {
    backTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ────── ハンバーガー ──────
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('nav-locked', open);
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-locked');
      });
    });
  }

  // ────── スクロールフェードイン ──────
  if (typeof window.IntersectionObserver === 'undefined') return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var targets = document.querySelectorAll('.section, .page-hero, .hero, .greeting-grid, .course-row, .service-tile, .flow-row, .faq-item, .news-card, .news-item');
  targets.forEach(function (el) { el.classList.add('fade-in'); });
  // services-grid の中の service-tile には index ベースの遅延を付与してステガード
  document.querySelectorAll('.services-grid').forEach(function (g) {
    g.querySelectorAll('.service-tile').forEach(function (tile, i) {
      tile.style.transitionDelay = (i * 90) + 'ms';
    });
  });
  document.querySelectorAll('.usp-grid').forEach(function (g) {
    g.querySelectorAll('.usp-cell').forEach(function (cell, i) {
      cell.classList.add('fade-in');
      cell.style.transitionDelay = (i * 90) + 'ms';
    });
  });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -10% 0px' });
  targets.forEach(function (el) { io.observe(el); });
  document.querySelectorAll('.usp-cell.fade-in').forEach(function (el) { io.observe(el); });
  // ファーストビューは即時表示
  setTimeout(function () {
    document.querySelectorAll('.hero, .page-hero').forEach(function (el) { el.classList.add('is-visible'); });
  }, 50);

  // ────── お問い合わせフォームを mailto: にハイジャック (Cloudflare Pages 移行前の暫定) ──────
  var form = document.querySelector('.contact-form');
  if (form && form.getAttribute('action') === '#mailto') {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var get = function (name) {
        var el = form.querySelector('[name="' + name + '"]');
        return el ? (el.value || '').trim() : '';
      };
      var company = get('company'), name = get('name'), email = get('email'), msg = get('message');
      var subject = '[horiz-ai.com お問い合わせ] ' + (company || '会社名未入力');
      var body =
        '会社名: ' + company + '\\n' +
        'ご担当者名: ' + name + '\\n' +
        'メールアドレス: ' + email + '\\n\\n' +
        'お問い合わせ内容:\\n' + msg + '\\n';
      var to = 'horiz.hokudai@gmail.com';
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      // ステータスメッセージ表示
      var status = form.querySelector('.form-status');
      if (status) status.classList.add('is-visible');
    });
  }
})();
</script>'''


def shell(title, description, body, active, body_class="", canonical_path=None, extra_jsonld=""):
    canonical = SITE_URL.rstrip("/") + (canonical_path or active or "/")
    service_jsonld = JSONLD_SERVICES.get(active, "")
    return f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
// WebP サポート検出 — 検出できたら <html> に webp-supported クラスを付与
(function () {{
  var img = new Image();
  img.onload = img.onerror = function () {{
    if (img.height === 2) document.documentElement.classList.add('webp-supported');
  }};
  img.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
}})();
</script>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/assets/images/icon.png">

<!-- Open Graph -->
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:site_name" content="株式会社horiz">
<meta property="og:locale" content="ja_JP">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{OG_IMAGE}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://horiz-ai.com">
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600;700&family=Noto+Sans+JP:wght@300;400;500;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={ASSET_VERSION}">
{f'<link rel="preload" as="image" href="/assets/images/home_hero.webp" type="image/webp" fetchpriority="high"><link rel="preload" as="image" href="/assets/images/home_hero.png" fetchpriority="high">' if active == "/" else ""}
{f'<link rel="preload" as="image" href="/assets/images/training_hero.webp" type="image/webp" fetchpriority="high">' if active == "/training/" else ""}
{f'<link rel="preload" as="image" href="/assets/images/consulting_hero.webp" type="image/webp" fetchpriority="high">' if active == "/consulting/" else ""}
{f'<link rel="preload" as="image" href="/assets/images/development_hero.webp" type="image/webp" fetchpriority="high">' if active == "/development/" else ""}

{JSONLD_ORGANIZATION}
{service_jsonld}
{extra_jsonld}
</head>
<body class="{body_class}">
<a class="skip-link" href="#main">本文へスキップ</a>
{scroll_progress()}
{header(active)}
<main id="main" tabindex="-1">
{body}
</main>
{footer()}
{back_to_top()}
{floating_cta()}
{SITE_JS}
</body>
</html>
'''


# ────────────────────────────────────────────────────────────────────────────
# 共通パーツ
# ────────────────────────────────────────────────────────────────────────────

def cta_pill(label="今すぐ無料相談！", href="/contact/"):
    return f'<div class="cta-pill-wrap"><a class="cta-pill" href="{href}">{label}</a></div>'


def picture(src, alt, cls=""):
    """`<picture>` で WebP 優先、PNG/JPG フォールバック。
    src は assets/images からの相対 (例: "svc_training.png") を期待。
    """
    base, _, ext = src.rpartition('.')
    cls_attr = f' class="{cls}"' if cls else ''
    return (
        f'<picture>'
        f'<source srcset="/assets/images/{base}.webp" type="image/webp">'
        f'<img src="/assets/images/{src}" alt="{alt}"{cls_attr} loading="lazy" decoding="async">'
        f'</picture>'
    )


def scroll_indicator():
    return '<div class="scroll-indicator" aria-hidden="true"><span class="scroll-indicator-line"></span></div>'


def breadcrumbs(trail):
    """trail: [(label, href or None), ...] — 末尾は現在地で href=None."""
    if not trail:
        return ""
    items_html = []
    jsonld_items = []
    for i, (label, href) in enumerate(trail):
        if href and i < len(trail) - 1:
            items_html.append(f'<li class="crumb"><a href="{href}">{label}</a></li>')
        else:
            items_html.append(f'<li class="crumb crumb-current" aria-current="page">{label}</li>')
        item = {"@type": "ListItem", "position": i + 1, "name": label}
        if href:
            item["item"] = SITE_URL.rstrip("/") + href
        jsonld_items.append(item)
    import json as _json
    jsonld = _json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": jsonld_items,
    }, ensure_ascii=False)
    return (
        f'<nav class="breadcrumbs" aria-label="パンくずリスト">'
        f'<ol class="crumb-list">{"".join(items_html)}</ol>'
        f'</nav>'
        f'<script type="application/ld+json">{jsonld}</script>'
    )


def floating_cta():
    """モバイル下部固定 CTA。"""
    return '<a class="floating-cta" href="/contact/">無料相談 →</a>'


def back_to_top():
    return '<button class="back-to-top" aria-label="ページトップへ戻る" type="button"><span aria-hidden="true">↑</span></button>'


def contact_form():
    return '''
<section class="section section-contact" id="contact">
  <div class="container">
    <h2 class="section-title">お問い合わせ</h2>
    <form class="contact-form" action="#mailto" method="post">
      <div class="form-row">
        <label class="form-label" for="company">会社名<span class="req">*</span></label>
        <input type="text" id="company" name="company" placeholder="株式会社horiz" required>
      </div>
      <div class="form-row">
        <label class="form-label" for="name">ご担当者名<span class="req">*</span></label>
        <input type="text" id="name" name="name" placeholder="ホライズ　太郎" required>
      </div>
      <div class="form-row">
        <label class="form-label" for="email">メールアドレス<span class="req">*</span></label>
        <input type="email" id="email" name="email" placeholder="info@horiz.com" required>
      </div>
      <div class="form-row">
        <label class="form-label" for="message">お問い合わせ内容<span class="req">*</span></label>
        <textarea id="message" name="message" rows="5" placeholder="なんでもお気軽にご連絡下さい。" required></textarea>
      </div>
      <button class="form-submit" type="submit">送信</button>
      <div class="form-status" role="status" aria-live="polite">
        <strong>メールアプリを開きました。</strong> 内容を確認のうえ送信してください。<br>
        メールアプリが起動しない場合は、お手数ですが <a href="mailto:horiz.hokudai@gmail.com">horiz.hokudai@gmail.com</a> 宛にお送りください。
      </div>
    </form>
  </div>
</section>'''


# ────────────────────────────────────────────────────────────────────────────
# 1. トップ
# ────────────────────────────────────────────────────────────────────────────

def home():
    title = "札幌のAI/DX研修・コンサル | 株式会社horiz"
    description = "中小企業に AI の進化を届ける。AI/DX法人研修、コンサルティング、AIシステム開発をワンストップで支援。札幌・北海道発、北大認定スタートアップ。"

    body = f'''
<section class="hero hero-home bg-home">
  <div class="hero-inner hero-home-inner">
    <div class="hero-text">
      <h1 class="hero-title">
        <span class="hero-line">中小企業に</span>
        <span class="hero-line"><span class="accent-teal">AI</span>の進化を届ける</span>
      </h1>
      <p class="hero-lede">DX・AI導入を、コンサルから開発・<br>人材育成までワンストップで支援</p>
    </div>
  </div>
  {scroll_indicator()}
</section>

<section class="section section-hus">
  <div class="container">
    <h2 class="section-title">北大発認定<br>スタートアップ企業</h2>
    <p class="hus-body">北大発認定スタートアップ企業への称号付与制度は、北大のスタートアップ・エコシステムの一員として、北大と共に成長してくださる企業様を申請の対象としています。</p>
    <div class="hus-lockup">
      ''' + picture("logo_white.png", "horiz", "hus-horiz") + '''
      <span class="hus-x">×</span>
      ''' + picture("hus_logo.png", "HOKKAIDO UNIVERSITY START UP", "hus-img") + '''
    </div>
  </div>
</section>

<section class="section section-services">
  <div class="container">
    <h2 class="section-title">事業内容</h2>
    <div class="services-grid">
      <a class="service-tile" href="/training/">
        <div class="service-image">''' + picture("svc_training.png", "企業研修") + '''</div>
        <h3 class="service-title">企業研修</h3>
        <p class="service-body">企業内でAIやDX、データサイエンスに特化した人材を育てるお手伝いをします。オンラインでの講座がメインですが、札幌近郊であれば対面での講座も可能です。</p>
      </a>
      <a class="service-tile" href="/consulting/">
        <div class="service-image">''' + picture("svc_consulting.png", "AI/DXコンサルティング") + '''</div>
        <h3 class="service-title">AI/DXコンサルティング</h3>
        <p class="service-body">毎日の面倒な作業はAIを使って自動化できます。大小さまざまな課題を抱えているお客様から、どんなことができるか聞いてみたいお客様まで、ぜひ一度ご相談ください。</p>
      </a>
      <a class="service-tile" href="/development/">
        <div class="service-image">''' + picture("svc_development.png", "AIシステム開発") + '''</div>
        <h3 class="service-title">AIシステム開発</h3>
        <p class="service-body">自社専用のチャットボットやカメラによる監視システム、データ分析など、作りたいものや解決したい課題が明確なお客様に対してソリューションを提供します。</p>
      </a>
    </div>
  </div>
</section>

<section class="section section-news-teaser">
  <div class="container">
    <h2 class="section-title">お知らせ</h2>
    <div class="news-teaser">
      <a class="news-card" href="/news/">
        <div class="news-image">''' + picture("case_forecast.jpg", "") + '''</div>
        <h3 class="news-title">株式会社horizの設立と事業概要</h3>
        <p class="news-date">4/3/2025</p>
      </a>
    </div>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/", body_class="page-home")


# ────────────────────────────────────────────────────────────────────────────
# 2. 会社概要
# ────────────────────────────────────────────────────────────────────────────

def about():
    title = "会社概要｜北大発のAI/DXパートナー | 株式会社horiz"
    description = "株式会社horizは、AI・DX領域に特化したテクノロジー企業。深層学習・画像処理を専門とするチームが、最先端のAI技術を社会に還元します。札幌・北海道発、北大認定スタートアップ。"

    # ────────────────────────────────────────────────────────
    # 代表挨拶セクション (プレースホルダ)
    #
    # 西浦さん本人にここを差し替えていただく:
    #   - ceo_name      : フルネーム
    #   - greeting_*    : 挨拶文 (見出し + 本文)
    #   - ceo_photo     : assets/images/ceo_portrait.jpg を配置すれば自動表示
    #
    # 写真が無い間は "PHOTO COMING SOON" プレースホルダが出る (img onerror)。
    # ────────────────────────────────────────────────────────
    ceo_name = "西浦 翼"
    ceo_role = "REPRESENTATIVE DIRECTOR"
    ceo_role_jp = "代表取締役"
    ceo_photo_jpg = "/assets/images/ceo_portrait.jpg"
    ceo_photo_webp = "/assets/images/ceo_portrait.webp"
    # NOTE: 当たり障りない暫定文面。西浦さん本人の文面が決まり次第差し替え。
    greeting_headline = "中小企業のAI活用、<br>最初のパートナーへ。"
    greeting_paragraphs = [
        "株式会社horizは、AI・DX領域に特化したテクノロジー企業です。最先端のAI技術を中小企業のみなさまにお届けすることを使命としています。",
        "AIやDXは、もはや一部の大企業だけのものではありません。日々の業務を整理し、データの力を活かすことで、現場の生産性は確実に変わります。研修・コンサルティング・システム開発の3本柱で、課題発見から実装・運用まで一貫してご支援いたします。",
        "北海道大学発の認定スタートアップとして、地域の企業様と共に歩み、確かな AI 活用の最初の一歩をお届けします。お気軽にご相談ください。",
    ]
    greeting_body_html = "".join(f"<p class=\"greeting-body\">{p}</p>" for p in greeting_paragraphs)

    body = breadcrumbs([("Home", "/"), ("会社概要", None)]) + f'''
<section class="page-hero page-hero-plain">
  <div class="container">
    <h1 class="page-hero-title">会社概要</h1>
  </div>
</section>

<section class="section section-about">
  <div class="container narrow">
    <p class="about-lead">horizは、AI・DX領域に特化したテクノロジー企業です。深層学習・画像処理を専門とするチームが、最先端のAI技術を社会に還元することを目指しています。</p>
  </div>
</section>

<section class="section section-greeting" id="greeting">
  <div class="container narrow">
    <h2 class="section-title">代表挨拶</h2>
    <div class="greeting-grid">
      <div class="greeting-photo">
        <picture>
          <source srcset="{ceo_photo_webp}" type="image/webp">
          <img src="{ceo_photo_jpg}" alt="代表 {ceo_name}" loading="lazy" decoding="async" onerror="this.style.display='none';this.parentElement.parentElement.querySelector('.greeting-photo-placeholder').style.display='block';">
        </picture>
        <span class="greeting-photo-placeholder" style="display:none;">PHOTO COMING SOON</span>
      </div>
      <div class="greeting-text">
        <p class="greeting-headline">{greeting_headline}</p>
        {greeting_body_html}
        <div class="greeting-signature">
          <p class="greeting-role">{ceo_role} · {ceo_role_jp}</p>
          <p class="greeting-name">{ceo_name}</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-info">
  <div class="container narrow">
    <h2 class="section-title">会社情報</h2>
    <table class="info-table">
      <tr><th>会社名</th><td>株式会社horiz</td></tr>
      <tr><th>代表者</th><td>西浦 翼</td></tr>
      <tr><th>設立</th><td>2025年3月10日</td></tr>
      <tr><th>資本金</th><td>100万円</td></tr>
      <tr><th>所在地</th><td>〒001-0012<br>北海道札幌市北区北12条西1丁目</td></tr>
    </table>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/about/", body_class="page-inner")


# ────────────────────────────────────────────────────────────────────────────
# 3. 企業研修
# ────────────────────────────────────────────────────────────────────────────

def training():
    title = "AI研修・生成AI企業研修｜札幌 | 株式会社horiz"
    description = "生成AIを学んで社内DXを達成。社内で専門的なAI人材を育成。助成金で研修費最大75%OFF。札幌発、オンライン全国対応の企業研修。"

    courses_basic = [
        ("DX",       "course_dx.jpg",    "「DXとは何か」から始まり、必要性や推進における課題などの基礎知識、最新事例や実際のデータ分析などの応用までを学習することができます。"),
        ("AI基礎",   "course_ai.png",    "今話題のAIについて、その歴史や仕組み、AIを用いたシステムやアプリケーションなどの事例について学習することができます。"),
        ("生成AI",   "course_genai.jpg", "近年サービスとして急速に広がっている生成AIについて、サービスの概要やその基本的な使い方、業務への展開など幅広く学習することができます。"),
    ]
    courses_pro = [
        ("データサイエンス基礎", "course_ds.jpg", "データ活用の第一歩として、データサイエンスの基本的な考え方や分析手法、データの可視化・統計的処理などについて学習することができます。"),
        ("機械学習",            "course_ml.jpg", "AIの中核技術である機械学習について、教師あり・教師なし学習などの基本概念から、代表的なアルゴリズムや実装の流れまでを学習することができます。"),
        ("深層学習",            "course_dl.png", "画像認識や自然言語処理などで用いられる深層学習の仕組みについて、ニューラルネットワークの基本構造から代表的なモデルまでを体系的に学習できます。実務への応用に向けた基礎固めを行います。"),
        ("画像処理",            "course_cv.jpg", "画像処理の基本的な手法から、AIと組み合わせた応用（人物検出・物体認識など）まで、幅広く学習できます。画像データの前処理や特徴抽出の技術を理解し、実際に使えるスキルの習得を目指します。"),
    ]

    def course_rows(courses):
        rows = []
        for title_, img, desc in courses:
            rows.append(
                '<div class="course-row">'
                f'<div class="course-image">{picture(img, title_)}</div>'
                f'<div class="course-text"><h3 class="course-title">{title_}</h3>'
                f'<p class="course-body">{desc}</p></div>'
                '</div>'
            )
        return ''.join(rows)

    body = breadcrumbs([("Home", "/"), ("事業内容", None), ("企業研修", None)]) + f'''
<section class="page-hero page-hero-photo bg-training">
  <div class="page-hero-overlay"></div>
  <div class="container">
    <h1 class="page-hero-title">企業研修</h1>
    <div class="usp-grid">
      <div class="usp-cell"><span class="usp-num">01</span><p class="usp-text">生成AIを学んで社内DXを達成</p></div>
      <div class="usp-cell"><span class="usp-num">02</span><p class="usp-text">社内で専門的なAI人材を育成</p></div>
      <div class="usp-cell"><span class="usp-num">03</span><p class="usp-text">助成金で研修費最大75%OFF</p></div>
    </div>
  </div>
</section>

<section class="cta-band">{cta_pill()}</section>

<section class="section section-courses">
  <div class="container">
    <h2 class="section-title">DX/生成AI</h2>
    <p class="section-lede">何ができるか知りたいという方は、まずこちらから！</p>
    <div class="course-list">{course_rows(courses_basic)}</div>
  </div>
</section>

<section class="section section-courses">
  <div class="container">
    <h2 class="section-title">データサイエンティスト<br>／AI人材育成</h2>
    <p class="section-lede">社内にAI部門を作りたい、スペシャリストを育成したいという方はこちら！</p>
    <div class="course-list">{course_rows(courses_pro)}</div>
  </div>
</section>

<section class="section section-pricing">
  <div class="container narrow">
    <h2 class="section-title">料金体系</h2>
    <p class="section-lede">受講者数や時間数によって変動します。ご予算に合わせたご提案もできますので、お気軽にご相談ください。</p>
  </div>
</section>

<section class="section section-subsidy">
  <div class="container narrow">
    <h2 class="section-title">助成金</h2>
    <p class="subsidy-lead">厚生労働省の「人材開発支援助成金」をご活用いただけます。</p>
    <h3 class="subsidy-sub">事業展開等リスキリング支援コース</h3>
    <table class="subsidy-table">
      <thead>
        <tr><th></th><th>経費助成</th><th>賃金助成</th></tr>
      </thead>
      <tbody>
        <tr><th class="subsidy-row-label">中小企業</th><td>75%</td><td>1,000円（1人1時間）</td></tr>
        <tr><th class="subsidy-row-label">大企業</th><td>60%</td><td>500円（1人1時間）</td></tr>
      </tbody>
    </table>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/training/", body_class="page-inner")


# ────────────────────────────────────────────────────────────────────────────
# 4. AI/DXコンサルティング
# ────────────────────────────────────────────────────────────────────────────

def consulting():
    title = "AI/DXコンサルティング｜札幌・北海道の中小企業伴走支援 | 株式会社horiz"
    description = "社内のDXを進め業務効率化、AI導入で課題解決。IT導入補助金・ものづくり補助金の活用支援も。札幌発、全国対応のAI/DXコンサルティング。"

    flow_steps = [
        ("1.無料相談", "オンラインまたは対面でお客様の課題や実現したいことを伺います。"),
        ("2.ご提案", "要件を整理し、支援内容やスケジュールをご提案いたします。"),
        ("3.ご契約・ご発注", "本サービスに関するご契約書に記入いただき、正式なご発注とさせていただきます。"),
        ("4.ヒアリング", "現状や業務課題をヒアリング・分析し、業務フローを作成いたします。"),
        ("5.DX推進・AI導入プランの作成", "業務フローをもとに、デジタル化や自動化を提案いたします。"),
        ("6.実行支援 & 導入サポート", "業務アプリや端末を実際に導入し、スタッフへのトレーニングも行います。"),
        ("7.運用・改善", "導入後の運用サポートや効果測定、必要に応じて改善提案を行います。"),
    ]

    flow_html = ''.join(
        f'<div class="flow-row"><h3 class="flow-title">{t}</h3><p class="flow-body">{b}</p></div>'
        for t, b in flow_steps
    )

    body = breadcrumbs([("Home", "/"), ("事業内容", None), ("AI/DXコンサルティング", None)]) + f'''
<section class="page-hero page-hero-photo bg-consulting">
  <div class="page-hero-overlay"></div>
  <div class="container">
    <h1 class="page-hero-title">AI/DXコンサルティング</h1>
    <div class="usp-grid">
      <div class="usp-cell"><span class="usp-num">01</span><p class="usp-text">社内のDXを進め業務効率化</p></div>
      <div class="usp-cell"><span class="usp-num">02</span><p class="usp-text">AI導入で課題解決</p></div>
      <div class="usp-cell"><span class="usp-num">03</span><p class="usp-text">助成金で低コストに実現</p></div>
    </div>
  </div>
</section>

<section class="cta-band">{cta_pill()}</section>

<section class="section section-flow">
  <div class="container narrow">
    <h2 class="section-title">DX推進・AI導入の流れ</h2>
    <div class="flow-list">{flow_html}</div>
  </div>
</section>

<section class="section section-subsidy">
  <div class="container narrow">
    <h2 class="section-title">補助金</h2>
    <ul class="subsidy-bullets">
      <li>IT導入補助金</li>
      <li>ものづくり補助金 など</li>
    </ul>
    <p class="subsidy-note">企業規模や指定のツールを使うなど、条件を満たせば申請できる補助金があります。お問い合わせいただければ、ご提案いたします。</p>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/consulting/", body_class="page-inner")


# ────────────────────────────────────────────────────────────────────────────
# 5. システム開発
# ────────────────────────────────────────────────────────────────────────────

def development():
    title = "AIシステム開発（画像認識・需要予測）| 株式会社horiz"
    description = "自社独自のAIシステムを開発。画像処理や時系列データなど高い専門性を持つ博士課程出身のエンジニアが、PoCから運用までワンストップで支援。"

    cases = [
        ("チャットボット", "case_chatbot.jpg",   "社内ヘルプデスクやカスタマー対応に、自然言語処理を活用したチャットボットを導入。よくある質問に自動対応し、対応時間と担当者の負担を削減します。"),
        ("画像処理",       "case_imageproc.jpg", "カメラ映像から人物検出や作業状態を認識するAIを導入。現場での安全管理や業務記録を自動化し、ミスの防止と品質向上を支援します。"),
        ("需要予測",       "case_forecast.jpg",  "販売データや気象情報をもとに、AIで需要を予測。小売・物流業界にて在庫や発注の最適化を実現し、コスト削減と売上向上を図ります。"),
    ]

    case_html = ''
    for title_, img, desc in cases:
        case_html += (
            '<div class="course-row">'
            f'<div class="course-image">{picture(img, title_)}</div>'
            f'<div class="course-text"><h3 class="course-title">{title_}</h3>'
            f'<p class="course-body">{desc}</p></div>'
            '</div>'
        )

    body = breadcrumbs([("Home", "/"), ("事業内容", None), ("システム開発", None)]) + f'''
<section class="page-hero page-hero-photo bg-development">
  <div class="page-hero-overlay"></div>
  <div class="container">
    <h1 class="page-hero-title">システム開発</h1>
    <div class="usp-grid">
      <div class="usp-cell"><span class="usp-num">01</span><p class="usp-text">自社独自のAIシステムを開発</p></div>
      <div class="usp-cell"><span class="usp-num">02</span><p class="usp-text">画像処理や時系列データなど高い専門性</p></div>
      <div class="usp-cell"><span class="usp-num">03</span><p class="usp-text">PoCから運用までワンストップで支援</p></div>
    </div>
  </div>
</section>

<section class="cta-band">{cta_pill()}</section>

<section class="section section-cases">
  <div class="container">
    <h2 class="section-title">AI導入事例</h2>
    <div class="course-list">{case_html}</div>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/development/", body_class="page-inner")


# ────────────────────────────────────────────────────────────────────────────
# 6. お知らせ
# ────────────────────────────────────────────────────────────────────────────

def news():
    title = "お知らせ | 株式会社horiz"
    description = "株式会社horizからのお知らせ。プレスリリース、サービスアップデート、メディア掲載情報など。"

    # ────────────────────────────────────────
    # ニュース記事リスト。新規記事は先頭に追加してください。
    # 各エントリは (date, title, body, image_filename or None) のタプル。
    # body は HTML 可（<p> 自動ラップ）。
    # ────────────────────────────────────────
    posts = [
        (
            "2025-04-03",
            "株式会社horizの設立と事業概要",
            "株式会社horizを北海道札幌市にて設立しました。AI・DX領域に特化したテクノロジー企業として、法人研修・コンサルティング・システム開発の3本柱で事業を展開してまいります。",
            "case_forecast.jpg",
        ),
    ]

    items = []
    for date, post_title, post_body, img in posts:
        # date "2025-04-03" → "4/3/2025" 表記 (Hostinger 版踏襲)
        y, m, d = date.split("-")
        date_disp = f"{int(m)}/{int(d)}/{y}"
        img_html = f'<div class="news-item-image">{picture(img, "")}</div>' if img else ''
        items.append(f'''
    <article class="news-item">
      {img_html}
      <div class="news-item-text">
        <h2 class="news-item-title">{post_title}</h2>
        <p class="news-item-date">{date_disp}</p>
        <p class="news-item-body">{post_body}</p>
      </div>
    </article>''')

    body = breadcrumbs([("Home", "/"), ("お知らせ", None)]) + f'''
<section class="page-hero page-hero-plain">
  <div class="container">
    <h1 class="page-hero-title">お知らせ</h1>
  </div>
</section>

<section class="section section-news">
  <div class="container narrow">
    {''.join(items) if items else '<p class="news-empty">現在、お知らせはありません。今後、プレスリリースやサービスアップデートをこちらでお知らせします。</p>'}
  </div>
</section>
'''

    return shell(title, description, body, "/news/", body_class="page-inner")


# ────────────────────────────────────────────────────────────────────────────
# 7. FAQ
# ────────────────────────────────────────────────────────────────────────────

def faq():
    title = "FAQ | 株式会社horiz"
    description = "AI/DX法人研修・コンサルティング・システム開発に関するよくある質問。費用、期間、補助金、PoC、契約フローなど。"

    qa = [
        ("DXとAI導入の違いは？どちらから始めるべき？",
         "DX で業務とデータ基盤を整え、次に AI を組み込みましょう。データなしで AI を入れても精度が出ず ROI が悪化します。DX 現状診断を無料で実施するのでお問い合わせください。"),
        ("生成AI を社内利用するときのセキュリティ対策は？",
         "専用クラウドかオンプレミスでモデルを隔離してください。外部 API に機密データを送ると情報漏えいリスクが高まります。セキュリティ評価シートと社内ガイドライン雛形を提供します。"),
        ("企業研修を完全オンラインで受講できる？",
         "はい、Zoom とブラウザ演習環境で全国対応します。企業研修の日程調整はお問い合わせフォームから。"),
        ("企業研修の費用はどれくらいかかる？",
         "AI/DX基礎研修は 55,000円（2 時間）からです。カスタムコースは人数と日数（到達目標や内容）で変動します。具体的な御見積は企業研修ページ経由でご依頼ください。"),
        ("DX 補助金 2025 を活用して導入できますか？",
         "厚生労働省の「人材開発支援助成金」の申請を代行します。応募要件等を確認しますので、まずはご相談ください。"),
        ("システム開発のPoC は期間と予算はどのくらい？",
         "画像認識 PoC は 4〜6 週間・80〜150 万円が目安です。データ準備済みであれば、期間を短縮できます。案件内容によっても異なりますので、ご相談ください。"),
        ("契約までの流れを教えてください。",
         "無料相談 → ご提案 → 見積 → 契約の 4 ステップです。小規模案件は最短 2 週間で着手できます。まずお問い合わせページから面談可能な日時をご連絡ください。"),
        ("社内 DX 推進チームの立ち上げ支援はありますか？",
         "役員向けワークショップと現場研修をセットで提供。半年で KPI 設定から初期 PoC 実行まで伴走します。DXコンサルのページからご連絡ください。"),
    ]

    items_html = ''.join(
        f'<details class="faq-item"><summary class="faq-q"><span class="faq-q-mark">Q.</span><span>{q}</span></summary><div class="faq-a"><span class="faq-a-mark">A.</span><p>{a}</p></div></details>'
        for q, a in qa
    )

    # FAQPage JSON-LD (Google検索のリッチ結果対応)
    import json as _json
    faq_jsonld = '<script type="application/ld+json">' + _json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }, ensure_ascii=False) + "</script>"

    body = breadcrumbs([("Home", "/"), ("FAQ", None)]) + f'''
<section class="page-hero page-hero-plain">
  <div class="container">
    <h1 class="page-hero-title">FAQ</h1>
  </div>
</section>

<section class="section section-faq">
  <div class="container narrow">
    <div class="faq-list">{items_html}</div>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/faq/", body_class="page-inner", extra_jsonld=faq_jsonld)


# ────────────────────────────────────────────────────────────────────────────
# 8. お問い合わせ
# ────────────────────────────────────────────────────────────────────────────

def contact():
    title = "お問い合わせ | 株式会社horiz"
    description = "AI/DX法人研修・コンサルティング・システム開発のご相談はこちら。札幌発、全国対応。お気軽にお問い合わせください。"

    body = breadcrumbs([("Home", "/"), ("お問い合わせ", None)]) + '''
<section class="page-hero page-hero-plain">
  <div class="container">
    <h1 class="page-hero-title">お問い合わせ</h1>
    <p class="page-hero-lede">DX・AI導入のご相談を承っています。お気軽にお問い合わせください。</p>
  </div>
</section>
''' + contact_form()

    return shell(title, description, body, "/contact/", body_class="page-inner page-contact")


# ────────────────────────────────────────────────────────────────────────────
# 出力
# ────────────────────────────────────────────────────────────────────────────

def not_found():
    title = "ページが見つかりません | 株式会社horiz"
    description = "お探しのページは見つかりませんでした。トップページまたは事業内容ページからお探しください。"
    body = '''
<section class="page-hero page-hero-plain">
  <div class="container">
    <p class="not-found-code">404</p>
    <h1 class="page-hero-title">ページが見つかりません</h1>
    <p class="page-hero-lede">お探しのページは移動または削除された可能性があります。</p>
  </div>
</section>

<section class="section">
  <div class="container narrow" style="text-align:center;">
    <div class="cta-pill-wrap"><a class="cta-pill" href="/">トップに戻る</a></div>
  </div>
</section>
'''
    return shell(title, description, body, "/404", body_class="page-inner page-404")


PAGES = [
    ("index.html",            home),
    ("about/index.html",      about),
    ("training/index.html",   training),
    ("consulting/index.html", consulting),
    ("development/index.html", development),
    ("news/index.html",       news),
    ("faq/index.html",        faq),
    ("contact/index.html",    contact),
    ("404.html",              not_found),
]


def main():
    for path, fn in PAGES:
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
        html = fn()
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {path} ({len(html.encode('utf-8'))}b)")


if __name__ == "__main__":
    main()
