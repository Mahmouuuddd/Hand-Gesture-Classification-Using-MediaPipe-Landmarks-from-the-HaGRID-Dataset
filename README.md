<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hand Gesture Classification — Mahmoud</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #040810;
    --surface: #0a1220;
    --border: #1a2a40;
    --accent: #00e5ff;
    --accent2: #7c3aed;
    --accent3: #10b981;
    --text: #e2e8f0;
    --muted: #64748b;
    --mono: 'Space Mono', monospace;
    --sans: 'Syne', sans-serif;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    overflow-x: hidden;
    min-height: 100vh;
  }

  /* Grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
    z-index: 0;
  }

  /* Glowing orbs */
  .orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(120px);
    pointer-events: none;
    z-index: 0;
    animation: drift 12s ease-in-out infinite alternate;
  }
  .orb-1 { width: 500px; height: 500px; background: rgba(0,229,255,0.06); top: -150px; left: -100px; }
  .orb-2 { width: 400px; height: 400px; background: rgba(124,58,237,0.07); bottom: -100px; right: -100px; animation-delay: -6s; }
  @keyframes drift { to { transform: translate(40px, 30px); } }

  main { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 60px 24px 100px; }

  /* Header */
  header { margin-bottom: 64px; }

  .badge-row {
    display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 28px;
    animation: fadeUp 0.6s ease both;
  }
  .badge {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 2px;
    border: 1px solid;
  }
  .badge-cyan   { color: var(--accent);  border-color: rgba(0,229,255,0.3);  background: rgba(0,229,255,0.05); }
  .badge-purple { color: #a78bfa;         border-color: rgba(124,58,237,0.3); background: rgba(124,58,237,0.05); }
  .badge-green  { color: var(--accent3);  border-color: rgba(16,185,129,0.3); background: rgba(16,185,129,0.05); }
  .badge-gray   { color: var(--muted);    border-color: var(--border);        background: transparent; }

  h1 {
    font-size: clamp(2.2rem, 6vw, 3.8rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.02em;
    margin-bottom: 20px;
    animation: fadeUp 0.6s 0.1s ease both;
  }
  h1 span { color: var(--accent); }

  .subtitle {
    font-size: 1.05rem;
    color: var(--muted);
    line-height: 1.7;
    max-width: 640px;
    animation: fadeUp 0.6s 0.2s ease both;
  }

  .github-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 28px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent);
    text-decoration: none;
    border: 1px solid rgba(0,229,255,0.3);
    padding: 10px 20px;
    border-radius: 2px;
    transition: background 0.2s, box-shadow 0.2s;
    animation: fadeUp 0.6s 0.3s ease both;
  }
  .github-link:hover {
    background: rgba(0,229,255,0.08);
    box-shadow: 0 0 20px rgba(0,229,255,0.15);
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* Divider */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 48px 0;
  }

  /* Section title */
  .section-label {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
    opacity: 0.7;
  }

  /* Pipeline */
  .pipeline {
    display: flex;
    align-items: center;
    gap: 0;
    margin-bottom: 48px;
    overflow-x: auto;
    padding-bottom: 8px;
  }
  .pipeline-step {
    flex: 1;
    min-width: 120px;
    text-align: center;
    padding: 20px 12px;
    border: 1px solid var(--border);
    background: var(--surface);
    position: relative;
  }
  .pipeline-step:first-child { border-radius: 4px 0 0 4px; }
  .pipeline-step:last-child  { border-radius: 0 4px 4px 0; }
  .pipeline-step + .pipeline-step { border-left: none; }
  .pipeline-step .icon { font-size: 1.5rem; margin-bottom: 8px; display: block; }
  .pipeline-step .label { font-size: 11px; font-family: var(--mono); color: var(--muted); }
  .pipeline-step .name  { font-size: 13px; font-weight: 600; color: var(--text); margin-top: 4px; }
  .pipeline-step.active { border-color: var(--accent); background: rgba(0,229,255,0.05); }
  .pipeline-step.active .name { color: var(--accent); }

  /* Stats grid */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin-bottom: 48px;
  }
  .stat-card {
    border: 1px solid var(--border);
    background: var(--surface);
    padding: 24px 20px;
    border-radius: 4px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
  }
  .stat-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,229,255,0.04), transparent);
    pointer-events: none;
  }
  .stat-card:hover { border-color: rgba(0,229,255,0.4); }
  .stat-value {
    font-family: var(--mono);
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
    margin-bottom: 6px;
  }
  .stat-label { font-size: 12px; color: var(--muted); letter-spacing: 0.05em; }
  .stat-sub { font-size: 10px; color: var(--border); font-family: var(--mono); margin-top: 4px; }

  /* Tech stack */
  .tech-list {
    display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 48px;
  }
  .tech-pill {
    font-family: var(--mono);
    font-size: 11px;
    padding: 6px 14px;
    border: 1px solid var(--border);
    border-radius: 2px;
    color: var(--text);
    background: var(--surface);
    display: flex; align-items: center; gap: 6px;
  }
  .tech-pill .dot {
    width: 6px; height: 6px; border-radius: 50%;
  }

  /* Feature list */
  .feature-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 48px;
  }
  @media (max-width: 600px) { .feature-grid { grid-template-columns: 1fr; } }

  .feature-item {
    border: 1px solid var(--border);
    background: var(--surface);
    padding: 18px 20px;
    border-radius: 4px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    transition: border-color 0.2s, transform 0.2s;
  }
  .feature-item:hover {
    border-color: rgba(124,58,237,0.5);
    transform: translateY(-2px);
  }
  .feature-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 2px; }
  .feature-title { font-size: 13px; font-weight: 600; margin-bottom: 4px; }
  .feature-desc  { font-size: 12px; color: var(--muted); line-height: 1.6; }

  /* Code block */
  .code-block {
    background: #020609;
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 48px;
  }
  .code-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    background: var(--surface);
  }
  .code-dots { display: flex; gap: 6px; }
  .code-dots span {
    width: 10px; height: 10px; border-radius: 50%;
  }
  .code-dots span:nth-child(1) { background: #ef4444; }
  .code-dots span:nth-child(2) { background: #f59e0b; }
  .code-dots span:nth-child(3) { background: #22c55e; }
  .code-filename { font-family: var(--mono); font-size: 11px; color: var(--muted); }
  pre {
    padding: 20px 20px;
    overflow-x: auto;
    font-family: var(--mono);
    font-size: 12px;
    line-height: 1.8;
    color: #94a3b8;
  }
  .kw  { color: #a78bfa; }
  .fn  { color: #60a5fa; }
  .st  { color: #34d399; }
  .cm  { color: #475569; }
  .nm  { color: var(--accent); }

  /* Gesture classes */
  .gesture-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 8px;
    margin-bottom: 48px;
  }
  .gesture-chip {
    border: 1px solid var(--border);
    background: var(--surface);
    border-radius: 3px;
    padding: 10px 8px;
    text-align: center;
    font-size: 11px;
    font-family: var(--mono);
    color: var(--muted);
    transition: all 0.2s;
    cursor: default;
  }
  .gesture-chip:hover {
    border-color: var(--accent3);
    color: var(--accent3);
    background: rgba(16,185,129,0.05);
  }
  .gesture-chip .emoji { font-size: 1.3rem; display: block; margin-bottom: 4px; }

  /* Author */
  .author-card {
    border: 1px solid var(--border);
    background: var(--surface);
    padding: 28px 24px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    gap: 20px;
  }
  .author-avatar {
    width: 56px; height: 56px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent2), var(--accent));
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    flex-shrink: 0;
  }
  .author-name { font-weight: 700; font-size: 1rem; margin-bottom: 4px; }
  .author-handle { font-family: var(--mono); font-size: 11px; color: var(--accent); }
  .author-bio { font-size: 12px; color: var(--muted); margin-top: 6px; }

  /* Scan line animation on stat cards */
  @keyframes scan {
    0%   { transform: translateY(-100%); }
    100% { transform: translateY(300%); }
  }
  .stat-card::before {
    content: '';
    position: absolute;
    left: 0; right: 0;
    height: 40%;
    background: linear-gradient(transparent, rgba(0,229,255,0.04), transparent);
    animation: scan 4s ease-in-out infinite;
    pointer-events: none;
  }
</style>
</head>
<body>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>

<main>

  <!-- Header -->
  <header>
    <div class="badge-row">
      <span class="badge badge-cyan">Computer Vision</span>
      <span class="badge badge-purple">Machine Learning</span>
      <span class="badge badge-green">Real-Time</span>
      <span class="badge badge-gray">Python</span>
      <span class="badge badge-gray">XGBoost</span>
    </div>

    <h1>Hand Gesture<br><span>Classification</span></h1>

    <p class="subtitle">
      Real-time gesture recognition using MediaPipe 3D landmark detection and XGBoost classification — trained on the HaGRID dataset with live webcam deployment via OpenCV.
    </p>

    <a href="https://github.com/Mahmouuuddd/Hand-Gesture-Classification-Using-MediaPipe-Landmarks-from-the-HaGRID-Dataset" class="github-link" target="_blank">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
      Mahmouuuddd / Hand-Gesture-Classification
    </a>
  </header>

  <div class="divider"></div>

  <!-- Pipeline -->
  <div class="section-label">// System Architecture</div>
  <div class="pipeline">
    <div class="pipeline-step">
      <span class="icon">🎥</span>
      <div class="label">Input</div>
      <div class="name">Webcam / HaGRID</div>
    </div>
    <div class="pipeline-step active">
      <span class="icon">🖐</span>
      <div class="label">Detection</div>
      <div class="name">MediaPipe</div>
    </div>
    <div class="pipeline-step">
      <span class="icon">📐</span>
      <div class="label">Preprocessing</div>
      <div class="name">Normalize</div>
    </div>
    <div class="pipeline-step active">
      <span class="icon">⚡</span>
      <div class="label">Classify</div>
      <div class="name">XGBoost</div>
    </div>
    <div class="pipeline-step">
      <span class="icon">📺</span>
      <div class="label">Output</div>
      <div class="name">Live Overlay</div>
    </div>
  </div>

  <!-- Stats -->
  <div class="section-label">// Metrics</div>
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">18</div>
      <div class="stat-label">Gesture Classes</div>
      <div class="stat-sub">hagrid dataset</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">63</div>
      <div class="stat-label">Input Features</div>
      <div class="stat-sub">21 landmarks × 3D xyz</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">F1</div>
      <div class="stat-label">Eval Metric</div>
      <div class="stat-sub">precision · recall</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">RT</div>
      <div class="stat-label">Real-Time</div>
      <div class="stat-sub">opencv streaming</div>
    </div>
  </div>

  <!-- Features -->
  <div class="section-label">// Key Features</div>
  <div class="feature-grid">
    <div class="feature-item">
      <div class="feature-icon">🗂</div>
      <div>
        <div class="feature-title">HaGRID Dataset</div>
        <div class="feature-desc">Large-scale hand gesture dataset with diverse gesture classes and real-world conditions.</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">🖐</div>
      <div>
        <div class="feature-title">MediaPipe Landmarks</div>
        <div class="feature-desc">21 hand keypoints in 3D (x, y, z) extracted per frame for robust spatial representation.</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">📏</div>
      <div>
        <div class="feature-title">Translation & Scale Norm</div>
        <div class="feature-desc">Preprocessing pipeline centers and normalizes landmarks, making features position-invariant.</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">⚡</div>
      <div>
        <div class="feature-title">XGBoost Classifier</div>
        <div class="feature-desc">Gradient boosted trees for fast, accurate multi-class gesture prediction at inference time.</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">📊</div>
      <div>
        <div class="feature-title">Full Evaluation Suite</div>
        <div class="feature-desc">F1 score, precision, recall, and confusion matrix analysis per gesture class.</div>
      </div>
    </div>
    <div class="feature-item">
      <div class="feature-icon">🎬</div>
      <div>
        <div class="feature-title">Live Webcam Demo</div>
        <div class="feature-desc">OpenCV streaming with real-time gesture overlay — prediction rendered directly on the video feed.</div>
      </div>
    </div>
  </div>

  <!-- Code -->
  <div class="section-label">// Inference Loop</div>
  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><span></span><span></span><span></span></div>
      <div class="code-filename">inference.py</div>
    </div>
    <pre><span class="kw">import</span> cv2, mediapipe <span class="kw">as</span> mp
<span class="kw">from</span> xgboost <span class="kw">import</span> XGBClassifier
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="fn">mp_hands</span> = mp.solutions.hands
model    = XGBClassifier()
model.<span class="fn">load_model</span>(<span class="st">'gesture_model.json'</span>)

cap = cv2.<span class="fn">VideoCapture</span>(<span class="nm">0</span>)

<span class="kw">with</span> mp_hands.Hands(<span class="nm">max_num_hands</span>=<span class="nm">1</span>) <span class="kw">as</span> hands:
    <span class="kw">while</span> cap.<span class="fn">isOpened</span>():
        ret, frame = cap.<span class="fn">read</span>()
        results    = hands.<span class="fn">process</span>(cv2.<span class="fn">cvtColor</span>(frame, cv2.COLOR_BGR2RGB))

        <span class="kw">if</span> results.multi_hand_landmarks:
            lm     = results.multi_hand_landmarks[<span class="nm">0</span>].landmark
            coords = np.<span class="fn">array</span>([[l.x, l.y, l.z] <span class="kw">for</span> l <span class="kw">in</span> lm])
            coords = (coords - coords[<span class="nm">0</span>]) / np.<span class="fn">max</span>(np.<span class="fn">abs</span>(coords))  <span class="cm"># normalize</span>
            pred   = model.<span class="fn">predict</span>(coords.<span class="fn">flatten</span>().<span class="fn">reshape</span>(<span class="nm">1</span>, -<span class="nm">1</span>))
            cv2.<span class="fn">putText</span>(frame, CLASSES[pred[<span class="nm">0</span>]], (<span class="nm">10</span>, <span class="nm">40</span>), ...)

        cv2.<span class="fn">imshow</span>(<span class="st">'Gesture Recognition'</span>, frame)</pre>
  </div>

  <!-- Gesture classes -->
  <div class="section-label">// Gesture Classes</div>
  <div class="gesture-grid">
    <div class="gesture-chip"><span class="emoji">✌️</span>peace</div>
    <div class="gesture-chip"><span class="emoji">👍</span>like</div>
    <div class="gesture-chip"><span class="emoji">👎</span>dislike</div>
    <div class="gesture-chip"><span class="emoji">✊</span>fist</div>
    <div class="gesture-chip"><span class="emoji">🖐</span>stop</div>
    <div class="gesture-chip"><span class="emoji">☝️</span>one</div>
    <div class="gesture-chip"><span class="emoji">🤞</span>crossed</div>
    <div class="gesture-chip"><span class="emoji">🤘</span>rock</div>
    <div class="gesture-chip"><span class="emoji">🖖</span>vulcan</div>
    <div class="gesture-chip"><span class="emoji">🤙</span>call</div>
    <div class="gesture-chip"><span class="emoji">👌</span>ok</div>
    <div class="gesture-chip"><span class="emoji">🤏</span>pinch</div>
    <div class="gesture-chip"><span class="emoji">💪</span>muscle</div>
    <div class="gesture-chip"><span class="emoji">🫵</span>point</div>
    <div class="gesture-chip"><span class="emoji">🖕</span>four</div>
    <div class="gesture-chip"><span class="emoji">🤟</span>love</div>
    <div class="gesture-chip"><span class="emoji">👐</span>open</div>
    <div class="gesture-chip"><span class="emoji">🤲</span>mute</div>
  </div>

  <!-- Tech Stack -->
  <div class="section-label">// Stack</div>
  <div class="tech-list">
    <div class="tech-pill"><span class="dot" style="background:#3b82f6"></span>Python</div>
    <div class="tech-pill"><span class="dot" style="background:#00e5ff"></span>MediaPipe</div>
    <div class="tech-pill"><span class="dot" style="background:#f59e0b"></span>XGBoost</div>
    <div class="tech-pill"><span class="dot" style="background:#10b981"></span>OpenCV</div>
    <div class="tech-pill"><span class="dot" style="background:#a78bfa"></span>NumPy</div>
    <div class="tech-pill"><span class="dot" style="background:#f472b6"></span>scikit-learn</div>
    <div class="tech-pill"><span class="dot" style="background:#fb923c"></span>Matplotlib</div>
    <div class="tech-pill"><span class="dot" style="background:#64748b"></span>HaGRID Dataset</div>
  </div>

  <div class="divider"></div>

  <!-- Author -->
  <div class="author-card">
    <div class="author-avatar">M</div>
    <div>
      <div class="author-name">Mahmoud</div>
      <div class="author-handle">@Mahmouuuddd</div>
      <div class="author-bio">Real-time computer vision · Hand landmark detection · Gesture ML pipelines</div>
    </div>
  </div>

</main>

</body>
</html>