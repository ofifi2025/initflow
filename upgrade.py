import re

with open('/sessions/focused-dazzling-keller/mnt/saas-tob-tracker/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ═══ 1. Replace CSS: AI Insight Card section ═══
old_css = """    /* AI Insight Card */
    .ai-insight-card { background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin-top:14px; }
    .ai-insight-header { display:flex; align-items:center; gap:8px; margin-bottom:14px; }
    .ai-icon { font-size:16px; }
    .ai-title { font-size:12px; font-weight:700; color:#1e293b; }
    .ai-insight-body { display:flex; flex-direction:column; gap:12px; }
    /* Input control well */
    .ai-input-row { display:flex; align-items:center; gap:8px; background:#f8fafc; border-radius:8px; padding:10px 14px; }
    .ai-input-row label { font-size:10px; font-weight:600; color:#94a3b8; white-space:nowrap; line-height:30px; text-transform:uppercase; letter-spacing:.3px; }
    .ai-input-row .ai-group { display:flex; align-items:center; gap:8px; }
    .ai-input-row .ai-group + .ai-group { margin-left:24px; }
    .ai-date-input { font-size:12px; padding:6px 12px; border:none; border-bottom:1.5px solid #e2e8f0; border-radius:0; color:#1e293b; outline:none; height:30px; min-width:140px; background:transparent; transition:border-color .15s; }
    .ai-date-input:focus { border-bottom-color:#6366f1; box-shadow:none; }
    .ai-btn { display:none; }
    .ai-output { font-size:12px; line-height:1.6; color:#475569; }"""

new_css = """    /* AI Insight Card — 4.0 SaaS Dashboard */
    .ai-insight-card { background:#fff; border:1px solid #F0F0F0; border-radius:16px; padding:24px; margin-top:14px; box-shadow:0 2px 12px rgba(0,0,0,0.04); }
    .ai-insight-header { display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; }
    .ai-header-left { display:flex; align-items:center; gap:8px; }
    .ai-header-right { display:flex; align-items:center; gap:12px; }
    .ai-icon { font-size:16px; }
    .ai-title { font-size:12px; font-weight:700; color:#1e293b; }
    .ai-insight-body { display:flex; flex-direction:column; gap:12px; }
    /* Date inputs — compact underline style in header */
    .ai-date-compact { position:relative; display:inline-flex; align-items:center; }
    .ai-date-compact input { font-size:12px; padding:4px 0; border:none; border-bottom:1px solid #e0e0e0; border-radius:0; color:#1e293b; outline:none; height:26px; width:110px; background:transparent; transition:all .15s; cursor:pointer; text-align:center; }
    .ai-date-compact input:focus { border-bottom-color:#6366f1; }
    .ai-date-compact input::-webkit-datetime-edit { color:transparent; }
    .ai-date-compact.has-value input::-webkit-datetime-edit { color:#1e293b; }
    .ai-date-placeholder { position:absolute; le; right:0; text-align:center; font-size:11px; color:#94a3b8; pointer-events:none; transition:opacity .15s; }
    .ai-date-compact.has-value .ai-date-placeholder { opacity:0; }
    .ai-date-compact input:focus + .ai-date-placeholder { opacity:0; }
    /* Breathing glow on empty date inputs */
    @keyframes breathe-glow { 0%,100%{box-shadow:0 1px 0 0 #e0e0e0} 50%{box-shadow:0 1px 6px 0 rgba(99,102,241,0.3)} }
    .ai-date-compact:not(.has-value) input { animation:breathe-glow 2.5s ease-in-out infinite; }
    .ai-btn { display:none; }
    .ai-output { font-size:12px; line-height:1.6; color:#475569; }
    /* Conclusion hero */
    .ai-conclusion-hero { text-align:center; padding:20px 0 18px; margin-bottom:16px; }
    .ai-conclusion-num { font-size:48px; font-weight:900; font-family:'SF Mono',SFMono-Regular,Menlo,Consolas,monospace; line-height:1; color:#cf1322; margin:4px 0; }
    .ai-conclusion-text { font-size:14px; font-weight:700; margin:0; }
    /* Dual column layout */
    .ai-dual-row { display:flex; align-items:stretch; margin-bottom:16px; }
    .ai-dual-left { flex:0 0 26%; padding:14px 16px; background:#FFF8F8; border-radius:10px; }
    .ai-dual-divider { border-right:1px dashed #e2e8f0; align-self:stretch; margin:0 18px; }
    .ai-dual-right { flex:1; min-width:0; }
    .ai-root-tag { display:inline-block; background:#FEE2E2; color:#cf1322; font-size:12px; font-weight:700; padding:3px 10px; border-radius:4px; cursor:pointer; transition:background .15s; }
    .ai-root-tag:hover { background:#FECACA; }
    /* CTA card */
    .ai-cta-card { background:linear-gradient(180deg,#F8FAFF 0%,#F0F4FF 100%); border:1px solid #E0E8FF; border-radius:12px; padding:16px 20px; margin-top:12px; }
    .ai-cta-btn { display:inline-flex; align-items:center; gap:6px; border-radius:8px; padding:10px 24px; font-size:12px; font-weight:700; border:none; cursor:pointer; transition:all .15s; }
    .ai-cta-btn.red { background:#cf1322; color:#fff; }
    .ai-cta-btn.red:hover { background:#a8071a; }
    .ai-cta-btn.blue { background:#3370FF; color:#fff; }
    .ai-cta-btn.blue:hover { background:#245bdb; }
    .ai-cta-hint { font-size:10px; color:#94a3b8; margin-top:4px; }
    /* Auto-promote toast */
    .auto-toast { position:fixed; top:16px; left:50%; transform:translateX(-50%); background:#ecfdf5; border:1px solid #86efac; color:#065f46; font-size:12px; font-weight:600; padding:8px 18px; border-radius:8px; z-index:99999; animation:toast-in .2s ease; }
    /* Error icon for blocked/overdue */
    .error-icon { display:inline-flex; align-items:center; justify-content:center; width:14px; height:14px; border-radius:50%; background:#cf1322; color:#fff; font-size:7px; font-weight:700; }
mpty state */
    .ai-empty-state { display:flex; flex-direction:column; align-items:center; justify-content:center; padding:40px 20px; background:linear-gradient(135deg, #f8faff 0%, #f0f4ff 50%, #faf5ff 100%); border-radius:12px; position:relative; overflow:hidden; }
    .ai-empty-state::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at 30% 20%, rgba(99,102,241,0.05) 0%, transparent 50%), radial-gradient(ellipse at 70% 80%, rgba(168,85,247,0.04) 0%, transparent 50%); pointer-events:none; }
    .ai-empty-icon { font-size:64px; line-height:1; margin-bott:16px; opacity:0.9; position:relative; }
    .ai-empty-title { font-size:15px; font-weight:700; color:#1e293b; margin-bottom:6px; position:relative; }
    .ai-empty-sub { font-size:12px; color:#94a3b8; position:relative; }
    .ai-skeleton { position:relative; margin-top:20px; width:100%; max-width:320px; }
    .ai-skeleton-line { height:8px; border-radius:4px; background:linear-gradient(90deg, #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%); background-size:200% 100%; animation:skeleton-shimmer 1.5s ease-in-out infinite; margin-bottom:8px; }
    @keyframes skeleton-shimmer { 0%{background-position:200% 0} 100%{background-position:-200% 0} }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("✓ CSS replaced")
else:
    print("✗ CSS not found")

print(f"File length after CSS: {len(content)}")
with open('/sessions/focused-dazzling-keller/mnt/saas-tob-tracker/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Step 1 done")
