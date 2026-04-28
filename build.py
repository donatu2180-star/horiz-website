#!/usr/bin/env python3
"""
horiz static site generator — production build.
Real Hostinger content, real images, polished editorial design.
"""
import pathlib

SITE = pathlib.Path("/Users/ryuki-izumi/Desktop/claude company/horiz-sales/marketing/seo/site")

def page(title, desc, depth, body):
    pre = "../" if depth == 1 else ""
    nav_active = body.get("nav", "")
    def nav_link(slug, label):
        cls = ' class="active"' if nav_active == slug else ''
        href = f"{pre}{slug}/"
        return f'<li><a href="{href}"{cls}>{label}</a></li>'
    nav_items = "\n      ".join([
        nav_link("about", "会社概要"),
        nav_link("training", "企業研修"),
        nav_link("consulting", "AI/DXコンサル"),
        nav_link("development", "システム開発"),
        nav_link("news", "お知らせ"),
        nav_link("faq", "FAQ"),
    ])
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+JP:wght@400;500;700&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
</head>
<body>

<header class="site-header">
  <nav class="nav">
    <a href="{pre}index.html" class="brand">
      <img src="{pre}assets/images/logo_white.png" alt="horiz" class="brand-logo">
    </a>
    <ul class="nav-links">
      {nav_items}
    </ul>
    <a href="{pre}contact/" class="nav-cta">無料相談 →</a>
  </nav>
</header>

<main>
{body['main']}
</main>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{pre}index.html" class="brand">
          <img src="{pre}assets/images/logo_white.png" alt="horiz" class="brand-logo">
        </a>
        <p>中小企業に AI の進化を届ける。<br>DX・AI導入を、コンサルから開発・人材育成までワンストップで支援。</p>
      </div>
      <div class="footer-col"><div class="footer-col-title">事業内容</div><ul>
        <li><a href="{pre}training/">企業研修</a></li>
        <li><a href="{pre}consulting/">AI/DXコンサルティング</a></li>
        <li><a href="{pre}development/">AIシステム開発</a></li>
      </ul></div>
      <div class="footer-col"><div class="footer-col-title">会社</div><ul>
        <li><a href="{pre}about/">会社概要</a></li>
        <li><a href="{pre}news/">お知らせ</a></li>
      </ul></div>
      <div class="footer-col"><div class="footer-col-title">サポート</div><ul>
        <li><a href="{pre}faq/">FAQ</a></li>
        <li><a href="{pre}contact/">お問い合わせ</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© 2025. All rights reserved.</span>
      <span>株式会社 horiz / Sapporo, Hokkaido</span>
    </div>
  </div>
</footer>

</body>
</html>
"""

# ============== HOME ==============
home_main = """
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-text">
        <div class="hero-meta">
          <span class="dot"></span>
          <span>北大発認定スタートアップ企業</span>
          <span class="dot"></span>
          <span class="quiet">Sapporo · Hokkaido</span>
        </div>
        <h1>
          中小企業に<br>
          <span class="accent">AI</span> の進化を届ける。
        </h1>
        <p class="hero-lede">
          DX・AI導入を、コンサルから開発・人材育成まで<br>ワンストップで支援。
        </p>
        <div class="hero-cta">
          <a href="contact/" class="btn btn-cream">無料相談を予約する <span class="arrow">→</span></a>
          <a href="#services" class="btn btn-ghost">事業内容を見る</a>
        </div>
      </div>
      <div class="hero-figure">
        <img src="assets/images/home_hero.png" alt="">
        <div class="hero-figure-tag">
          <span class="live-dot"></span>
          horiz · 北大発スタートアップ
        </div>
      </div>
    </div>
  </div>
</section>

<section class="testimonial">
  <div class="container">
    <div class="testimonial-card">
      <div class="testimonial-emblem">
        <img src="assets/images/hus_logo.png" alt="北海道大学">
      </div>
      <div class="testimonial-body">
        <h3>北大のスタートアップ・エコシステムの一員として、北大と共に<em>成長してくださる企業様</em>として認定。</h3>
        <p>北大発認定スタートアップ企業への称号付与制度は、北大のスタートアップ・エコシステムの一員として、北大と共に成長してくださる企業様を申請の対象としています。</p>
        <div class="testimonial-attribution">
          <div>
            <div class="label">Certified by</div>
            <div class="who">Hokkaido University</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="svc-section" id="services">
  <div class="container">
    <div class="eyebrow"><span class="num">— 02</span><span class="bar"></span><span>Services</span></div>
    <div class="svc-head">
      <h2 class="section-title">事業<em>内容</em></h2>
      <p class="lede">コンサルから開発・人材育成までワンストップで支援します。</p>
    </div>

    <div class="svc-grid">
      <a href="training/" class="svc-tile">
        <div class="svc-tile-img"><img src="assets/images/svc_training.png" alt=""></div>
        <div class="svc-tile-body">
          <span class="svc-tile-num">SVC 01</span>
          <h3>企業研修</h3>
          <span class="en">Corporate Training</span>
          <p>企業内でAIやDX、データサイエンスに特化した人材を育てるお手伝いをします。オンラインでの講座がメインですが、札幌近郊であれば対面での講座も可能です。</p>
          <span class="svc-tile-arrow">詳しく見る →</span>
        </div>
      </a>
      <a href="consulting/" class="svc-tile">
        <div class="svc-tile-img"><img src="assets/images/svc_consulting.png" alt=""></div>
        <div class="svc-tile-body">
          <span class="svc-tile-num">SVC 02</span>
          <h3>AI/DXコンサルティング</h3>
          <span class="en">Consulting</span>
          <p>毎日の面倒な作業はAIを使って自動化できます。大小さまざまな課題を抱えているお客様から、どんなことができるか聞いてみたいお客様まで、ぜひ一度ご相談ください。</p>
          <span class="svc-tile-arrow">詳しく見る →</span>
        </div>
      </a>
      <a href="development/" class="svc-tile">
        <div class="svc-tile-img"><img src="assets/images/svc_development.png" alt=""></div>
        <div class="svc-tile-body">
          <span class="svc-tile-num">SVC 03</span>
          <h3>AIシステム開発</h3>
          <span class="en">Development</span>
          <p>自社専用のチャットボットやカメラによる監視システム、データ分析など、作りたいものや解決したい課題が明確なお客様に対してソリューションを提供します。</p>
          <span class="svc-tile-arrow">詳しく見る →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 03</span><span class="bar"></span><span>Get Started</span></div>
        <h2 class="serif">まずは<em>無料相談</em>から。</h2>
        <p class="subtitle">DX・AI導入のご相談を承っています。お気軽にお問い合わせください。</p>
        <a href="contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Based in</div><div class="value">札幌・北海道</div></div>
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
        <div class="cta-info-item"><div class="label">Coverage</div><div class="value">全国対応</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== ABOUT ==============
about_main = """
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>会社概要</div>
    <div class="eyebrow"><span class="num">— 01</span><span class="bar"></span><span>About</span></div>
    <h1>会社<em>概要</em></h1>
  </div>
</section>

<section class="about-statement">
  <div class="container narrow">
    <p class="about-statement-text">
      horizは、AI・DX領域に特化したテクノロジー企業で、深層学習や画像処理を専門とする<em>博士課程の学生</em>により設立されました。最先端のAI技術を社会に還元することを目的にしています。
    </p>
    <div class="about-divider"></div>
    <div style="display:flex;gap:64px;flex-wrap:wrap;">
      <div>
        <div style="font-family:'Inter',sans-serif;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px;">Specialization</div>
        <div style="font-family:'Shippori Mincho',serif;font-size:18px;font-weight:500;">深層学習・画像処理</div>
      </div>
      <div>
        <div style="font-family:'Inter',sans-serif;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px;">Founded by</div>
        <div style="font-family:'Shippori Mincho',serif;font-size:18px;font-weight:500;">博士課程の学生</div>
      </div>
      <div>
        <div style="font-family:'Inter',sans-serif;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px;">Based in</div>
        <div style="font-family:'Shippori Mincho',serif;font-size:18px;font-weight:500;">札幌・北海道</div>
      </div>
    </div>
  </div>
</section>

<section class="testimonial">
  <div class="container">
    <div class="testimonial-card">
      <div class="testimonial-emblem">
        <img src="../assets/images/hus_logo.png" alt="北海道大学">
      </div>
      <div class="testimonial-body">
        <h3>北大発認定スタートアップ企業として、北大と共に<em>成長してくださる企業様</em>に認定。</h3>
        <p>北大発認定スタートアップ企業への称号付与制度は、北大のスタートアップ・エコシステムの一員として、北大と共に成長してくださる企業様を申請の対象としています。</p>
        <div class="testimonial-attribution">
          <div><div class="label">Certified by</div><div class="who">Hokkaido University</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 03</span><span class="bar"></span><span>Get in Touch</span></div>
        <h2>お<em>問い合わせ</em></h2>
        <p class="subtitle">ご相談・お問い合わせはお気軽にどうぞ。</p>
        <a href="../contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Based in</div><div class="value">札幌・北海道</div></div>
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== TRAINING ==============
training_main = """
<section class="page-hero with-bg">
  <div class="page-hero-bg"><img src="../assets/images/training_hero.jpg" alt=""></div>
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>事業内容<span class="sep">/</span>企業研修</div>
    <div class="eyebrow"><span class="num">— SVC 01</span><span class="bar"></span><span>Corporate Training</span></div>
    <h1>企業<em>研修</em></h1>
    <p class="lede">企業内でAIやDX、データサイエンスに特化した人材を育てるお手伝いをします。オンラインでの講座がメインですが、札幌近郊であれば対面での講座も可能です。</p>
    <div style="margin-top:40px;">
      <a href="../contact/" class="btn btn-cream">今すぐ無料相談！ <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="usp-section">
  <div class="container">
    <div class="usp-grid">
      <div class="usp-cell"><div class="usp-cell-text">生成AIを学んで社内DXを達成</div></div>
      <div class="usp-cell"><div class="usp-cell-text">社内で専門的なAI人材を育成</div></div>
      <div class="usp-cell"><div class="usp-cell-text">助成金で研修費最大75%OFF</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow"><span class="num">— 01</span><span class="bar"></span><span>Course Catalog · Foundation</span></div>
    <div class="catalog-head">
      <h2>DX/<em>生成AI</em></h2>
      <p class="lede">何ができるか知りたいという方は、まずこちらから！</p>
    </div>
    <div class="catalog-grid">
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_dx.jpg" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 01</span>
          <h3>DX</h3>
          <p>「DXとは何か」から始まり、必要性や推進における課題などの基礎知識、最新事例や実際のデータ分析などの応用までを学習することができます。</p>
        </div>
      </div>
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_ai.png" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 02</span>
          <h3>AI基礎</h3>
          <p>今話題のAIについて、その歴史や仕組み、AIを用いたシステムやアプリケーションなどの事例について学習することができます。</p>
        </div>
      </div>
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_genai.jpg" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 03</span>
          <h3>生成AI</h3>
          <p>近年サービスとして急速に広がっている生成AIについて、サービスの概要やその基本的な使い方、業務への展開など幅広く学習することができます。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="eyebrow"><span class="num">— 02</span><span class="bar"></span><span>Course Catalog · Specialist</span></div>
    <div class="catalog-head">
      <h2>データサイエンティスト／<em>AI人材育成</em></h2>
      <p class="lede">社内にAI部門を作りたい、スペシャリストを育成したいという方はこちら！</p>
    </div>
    <div class="catalog-grid cols-4">
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_ds.jpg" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 04</span>
          <h3>データサイエンス基礎</h3>
          <p>データ活用の第一歩として、データサイエンスの基本的な考え方や分析手法、データの可視化・統計的処理などについて学習することができます。</p>
        </div>
      </div>
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_ml.jpg" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 05</span>
          <h3>機械学習</h3>
          <p>AIの中核技術である機械学習について、教師あり・教師なし学習などの基本概念から、代表的なアルゴリズムや実装の流れまでを学習することができます。</p>
        </div>
      </div>
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_dl.png" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 06</span>
          <h3>深層学習</h3>
          <p>画像認識や自然言語処理などで用いられる深層学習の仕組みについて、ニューラルネットワークの基本構造から代表的なモデルまでを体系的に学習できます。実務への応用に向けた基礎固めを行います。</p>
        </div>
      </div>
      <div class="catalog-card">
        <div class="catalog-card-img"><img src="../assets/images/course_cv.jpg" alt=""></div>
        <div class="catalog-card-body">
          <span class="catalog-card-num">Course 07</span>
          <h3>画像処理</h3>
          <p>画像処理の基本的な手法から、AIと組み合わせた応用（人物検出・物体認識など）まで、幅広く学習できます。画像データの前処理や特徴抽出の技術を理解し、実際に使えるスキルの習得を目指します。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start;">
      <div>
        <div class="eyebrow"><span class="num">— 03</span><span class="bar"></span><span>Pricing</span></div>
        <h2 class="section-title">料金<em>体系</em></h2>
        <div class="simple-card">
          <span class="label">Pricing Note</span>
          <p>受講者数や時間数によって変動します。ご予算に合わせたご提案もできますので、お気軽にご相談ください。</p>
        </div>
      </div>
      <div>
        <div class="eyebrow"><span class="num">— 04</span><span class="bar"></span><span>Subsidy</span></div>
        <h2 class="section-title">助成金</h2>
        <p style="font-size:15.5px;color:var(--ink-2);line-height:1.95;margin-bottom:24px;">厚生労働省の「人材開発支援助成金」をご活用いただけます。</p>
        <div class="subsidy-callout">
          <span class="badge">活用可能コース</span>
          <h3>事業展開等リスキリング支援コース</h3>
          <span class="program-meta">厚生労働省 · 人材開発支援助成金</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 05</span><span class="bar"></span><span>Get Started</span></div>
        <h2>無料<em>相談</em></h2>
        <p class="subtitle">研修内容や助成金についてのご相談をお気軽にどうぞ。</p>
        <a href="../contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
        <div class="cta-info-item"><div class="label">Subsidy</div><div class="value">人材開発支援助成金</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== CONSULTING ==============
flow_steps = [
    ("1.無料相談", "オンラインまたは対面でお客様の課題や実現したいことを伺います。"),
    ("2.ご提案", "要件を整理し、支援内容やスケジュールをご提案いたします。"),
    ("3.ご契約・ご発注", "本サービスに関するご契約書に記入いただき、正式なご発注とさせていただきます。"),
    ("4.ヒアリング", "現状や業務課題をヒアリング・分析し、業務フローを作成いたします。"),
    ("5.DX推進・AI導入プランの作成", "業務フローをもとに、デジタル化や自動化を提案いたします。"),
    ("6.実行支援 & 導入サポート", "業務アプリや端末を実際に導入し、スタッフへのトレーニングも行います。"),
    ("7.運用・改善", "導入後の運用サポートや効果測定、必要に応じて改善提案を行います。"),
]
flow_html = "\n".join([
    f'<div class="flow-step"><div class="flow-step-title">{t}</div><div class="flow-step-body">{b}</div></div>'
    for t, b in flow_steps
])

consulting_main = f"""
<section class="page-hero with-bg">
  <div class="page-hero-bg"><img src="../assets/images/consulting_hero.jpg" alt=""></div>
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>事業内容<span class="sep">/</span>AI/DXコンサルティング</div>
    <div class="eyebrow"><span class="num">— SVC 02</span><span class="bar"></span><span>Consulting</span></div>
    <h1>AI/DX <em>コンサルティング</em></h1>
    <p class="lede">毎日の面倒な作業はAIを使って自動化できます。大小さまざまな課題を抱えているお客様から、どんなことができるか聞いてみたいお客様まで、ぜひ一度ご相談ください。</p>
    <div style="margin-top:40px;">
      <a href="../contact/" class="btn btn-cream">今すぐ無料相談！ <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="usp-section">
  <div class="container">
    <div class="usp-grid">
      <div class="usp-cell"><div class="usp-cell-text">社内のDXを進め業務効率化</div></div>
      <div class="usp-cell"><div class="usp-cell-text">AI導入で課題解決</div></div>
      <div class="usp-cell"><div class="usp-cell-text">助成金で低コストに実現</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow"><span class="num">— 01</span><span class="bar"></span><span>Process</span></div>
    <h2 class="section-title" style="text-align:center;">DX推進・AI導入の<em>流れ</em></h2>
    <div class="flow">
      {flow_html}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="eyebrow"><span class="num">— 02</span><span class="bar"></span><span>Subsidy</span></div>
    <h2 class="section-title">補助金</h2>
    <p class="section-lede">企業規模や指定のツールを使うなど、条件を満たせば申請できる補助金があります。お問い合わせいただければ、ご提案いたします。</p>
    <div class="chips">
      <span class="chip">IT導入補助金</span>
      <span class="chip">ものづくり補助金</span>
      <span class="chip dashed">など</span>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 03</span><span class="bar"></span><span>Get Started</span></div>
        <h2>無料<em>相談</em></h2>
        <p class="subtitle">DX推進・AI導入のご相談をお気軽にどうぞ。</p>
        <a href="../contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== DEVELOPMENT ==============
development_main = """
<section class="page-hero with-bg">
  <div class="page-hero-bg"><img src="../assets/images/development_hero.jpg" alt=""></div>
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>事業内容<span class="sep">/</span>AIシステム開発</div>
    <div class="eyebrow"><span class="num">— SVC 03</span><span class="bar"></span><span>Development</span></div>
    <h1>AIシステム<em>開発</em></h1>
    <p class="lede">自社専用のチャットボットやカメラによる監視システム、データ分析など、作りたいものや解決したい課題が明確なお客様に対してソリューションを提供します。</p>
    <div style="margin-top:40px;">
      <a href="../contact/" class="btn btn-cream">今すぐ無料相談！ <span class="arrow">→</span></a>
    </div>
  </div>
</section>

<section class="usp-section">
  <div class="container">
    <div class="usp-grid">
      <div class="usp-cell"><div class="usp-cell-text">自社独自のAIシステムを開発</div></div>
      <div class="usp-cell"><div class="usp-cell-text">画像処理や時系列データなど高い専門性</div></div>
      <div class="usp-cell"><div class="usp-cell-text">PoCから運用までワンストップで支援</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow"><span class="num">— 01</span><span class="bar"></span><span>Case Studies</span></div>
    <h2 class="section-title">AI<em>導入事例</em></h2>

    <div class="case">
      <div class="case-img">
        <span class="case-img-tag">CASE 01</span>
        <img src="../assets/images/case_chatbot.jpg" alt="">
      </div>
      <div class="case-body">
        <span class="num">Case 01 · NLP</span>
        <h3>チャットボット</h3>
        <p>社内ヘルプデスクやカスタマー対応に、自然言語処理を活用したチャットボットを導入。よくある質問に自動対応し、対応時間と担当者の負担を削減します。</p>
      </div>
    </div>

    <div class="case reverse">
      <div class="case-img">
        <span class="case-img-tag">CASE 02</span>
        <img src="../assets/images/case_imageproc.jpg" alt="">
      </div>
      <div class="case-body">
        <span class="num">Case 02 · Computer Vision</span>
        <h3>画像処理</h3>
        <p>カメラ映像から人物検出や作業状態を認識するAIを導入。現場での安全管理や業務記録を自動化し、ミスの防止と品質向上を支援します。</p>
      </div>
    </div>

    <div class="case">
      <div class="case-img">
        <span class="case-img-tag">CASE 03</span>
        <img src="../assets/images/case_forecast.jpg" alt="">
      </div>
      <div class="case-body">
        <span class="num">Case 03 · Forecasting</span>
        <h3>需要予測</h3>
        <p>販売データや気象情報をもとに、AIで需要を予測。小売・物流業界にて在庫や発注の最適化を実現し、コスト削減と売上向上を図ります。</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 02</span><span class="bar"></span><span>Get Started</span></div>
        <h2>無料<em>相談</em></h2>
        <p class="subtitle">AIシステム開発のご相談をお気軽にどうぞ。PoCからお試しいただけます。</p>
        <a href="../contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== FAQ ==============
faq_categories = [
    ("Strategy", [
        ("DXとAI導入の違いは？どちらから始めるべき？",
         "DX で業務とデータ基盤を整え、次に AI を組み込みましょう。データなしで AI を入れても精度が出ず ROI が悪化します。DX 現状診断を無料で実施するのでお問い合わせください。"),
        ("社内 DX 推進チームの立ち上げ支援はありますか？",
         "役員向けワークショップと現場研修をセットで提供。半年で KPI 設定から初期 PoC 実行まで伴走します。DXコンサルのページからご連絡ください。"),
        ("生成AI を社内利用するときのセキュリティ対策は？",
         "専用クラウドかオンプレミスでモデルを隔離してください。外部 API に機密データを送ると情報漏えいリスクが高まります。セキュリティ評価シートと社内ガイドライン雛形を提供します。"),
    ]),
    ("Training", [
        ("企業研修を完全オンラインで受講できる？",
         "はい、Zoom とブラウザ演習環境で全国対応します。企業研修の日程調整はお問い合わせフォームから。"),
        ("企業研修の費用はどれくらいかかる？",
         "AI/DX基礎研修は 55,000円（2 時間）からです。カスタムコースは人数と日数（到達目標や内容）で変動します。具体的な御見積は企業研修ページ経由でご依頼ください。"),
    ]),
    ("Subsidy & Contract", [
        ("DX 補助金 2025 を活用して導入できますか？",
         "厚生労働省の「人材開発支援助成金」の申請を代行します。応募要件等を確認しますので、まずはご相談ください。"),
        ("システム開発のPoC は期間と予算はどのくらい？",
         "画像認識 PoC は 4〜6 週間・80〜150 万円が目安です。データ準備済みであれば、期間を短縮できます。案件内容によっても異なりますので、ご相談ください。"),
        ("契約までの流れを教えてください。",
         "無料相談 → ご提案 → 見積 → 契約の 4 ステップです。小規模案件は最短 2 週間で着手できます。まずお問い合わせページから面談可能な日時をご連絡ください。"),
    ]),
]
faq_html = ""
for cat_label, items in faq_categories:
    faq_html += f'<div class="faq-cat" style="margin-top:64px;"><div style="font-family: Inter, sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.22em; color: var(--gold); text-transform: uppercase; margin-bottom: 16px;">— {cat_label}</div><div class="faq-list">'
    for q, a in items:
        faq_html += (
            f'<details class="faq-item">'
            f'<summary class="faq-summary">'
            f'<span class="faq-q-mark">Q</span>'
            f'<span class="faq-q-text">{q}</span>'
            f'<span class="faq-toggle"></span>'
            f'</summary>'
            f'<div class="faq-a">{a}</div>'
            f'</details>'
        )
    faq_html += "</div></div>"

faq_main = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>FAQ</div>
    <div class="eyebrow"><span class="num">— FAQ</span><span class="bar"></span><span>Frequently Asked</span></div>
    <h1>よくあるご<em>質問</em></h1>
    <p class="lede">DX、AI、生成AI、研修、補助金、PoCについて。掲載のないご質問はお気軽にお問い合わせください。</p>
  </div>
</section>

<section class="section">
  <div class="container narrow">
    {faq_html}
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <div class="cta-grid">
      <div>
        <div class="eyebrow"><span class="num">— 02</span><span class="bar"></span><span>Still Have Questions?</span></div>
        <h2>他にご質問が<em>あれば</em></h2>
        <p class="subtitle">掲載にないご質問もお気軽にお問い合わせください。</p>
        <a href="../contact/" class="btn btn-cream">お問い合わせ <span class="arrow">→</span></a>
      </div>
      <div class="cta-info">
        <div class="cta-info-item"><div class="label">Based in</div><div class="value">札幌・北海道</div></div>
        <div class="cta-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ============== NEWS ==============
news_main = """
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>お知らせ</div>
    <div class="eyebrow"><span class="num">— News</span><span class="bar"></span><span>Updates</span></div>
    <h1>お<em>知らせ</em></h1>
  </div>
</section>

<section class="section">
  <div class="container narrow">
    <div class="empty">
      <div class="empty-mark serif">—</div>
      <h3>現在、お知らせはありません。</h3>
      <p>今後、プレスリリースやサービスアップデートをこちらでお知らせします。</p>
    </div>
  </div>
</section>
"""

# ============== CONTACT ==============
contact_main = """
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a><span class="sep">/</span>お問い合わせ</div>
    <div class="eyebrow"><span class="num">— Contact</span><span class="bar"></span><span>Get Started</span></div>
    <h1>お<em>問い合わせ</em></h1>
    <p class="lede">DX・AI導入、企業研修、システム開発のご相談を承っています。</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <h2>無料相談を<br>受け付けています。</h2>
        <p>下記フォームからご連絡ください。お気軽にどうぞ。</p>
        <div class="contact-info-list">
          <div class="contact-info-item"><div class="label">Based in</div><div class="value">札幌・北海道</div></div>
          <div class="contact-info-item"><div class="label">Format</div><div class="value">オンライン／対面（札幌近郊）</div></div>
          <div class="contact-info-item"><div class="label">Coverage</div><div class="value">全国対応</div></div>
        </div>
      </div>

      <form class="form" action="#" method="post">
        <div class="form-row">
          <label>会社名<span class="req">*</span></label>
          <input type="text" name="company" required>
        </div>
        <div class="form-row">
          <label>ご担当者名<span class="req">*</span></label>
          <input type="text" name="name" required>
        </div>
        <div class="form-row">
          <label>メールアドレス<span class="req">*</span></label>
          <input type="email" name="email" required>
        </div>
        <div class="form-row">
          <label>お問い合わせ内容<span class="req">*</span></label>
          <textarea name="message" required></textarea>
        </div>
        <button type="submit" class="btn btn-fill" style="justify-self:start;">送信 <span class="arrow">→</span></button>
      </form>
    </div>
  </div>
</section>
"""

PAGES = [
    ("",              "index.html",            0, "株式会社horiz — 中小企業に AI の進化を届ける",                "中小企業にAIの進化を届ける。DX・AI導入を、コンサルから開発・人材育成までワンストップで支援。北大発認定スタートアップ企業 株式会社horiz。",         home_main),
    ("about",         "about/index.html",      1, "会社概要 — 株式会社horiz",                                        "horizは、AI・DX領域に特化したテクノロジー企業で、深層学習や画像処理を専門とする博士課程の学生により設立されました。",                                  about_main),
    ("training",      "training/index.html",   1, "企業研修 — 株式会社horiz",                                        "生成AIを学んで社内DXを達成。社内で専門的なAI人材を育成。助成金で研修費最大75%OFF。",                                                                  training_main),
    ("consulting",    "consulting/index.html", 1, "AI/DXコンサルティング — 株式会社horiz",                            "社内のDXを進め業務効率化、AI導入で課題解決、助成金で低コストに実現。",                                                                                  consulting_main),
    ("development",   "development/index.html",1, "AIシステム開発 — 株式会社horiz",                                  "自社独自のAIシステムを開発。画像処理や時系列データなど高い専門性。PoCから運用までワンストップで支援。",                                                  development_main),
    ("news",          "news/index.html",       1, "お知らせ — 株式会社horiz",                                        "株式会社horizからのお知らせ。",                                                                                                                          news_main),
    ("faq",           "faq/index.html",        1, "FAQ — 株式会社horiz",                                              "よくあるご質問。DX、AI、生成AI、企業研修、補助金、PoCについて。",                                                                                       faq_main),
    ("contact",       "contact/index.html",    1, "お問い合わせ — 株式会社horiz",                                    "無料相談・お問い合わせフォーム。",                                                                                                                       contact_main),
]

for nav, path, depth, title, desc, main in PAGES:
    full_path = SITE / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    html_str = page(title, desc, depth, {"nav": nav, "main": main})
    full_path.write_text(html_str, encoding="utf-8")
    print(f"wrote {path} ({len(html_str)}b)")
