import re, sys

with open('/sessions/focused-dazzling-keller/mnt/saas-tob-tracker/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Replace AI Insight Card HTML structure
old_html = (
    '<div class="ai-insight-card">\n'
    '  <div class="ai-insight-header">\n'
    '    <span class="ai-icon">\U0001f916</span>\n'
    '    <span class="ai-title">AI 进度洞察</span>\n'
    '  </div>\n'
    '  <div class="ai-insight-body">\n'
    '    <div class="ai-input-row">\n'
    '      <div class="ai-group">\n'
    '        <label for="start-date">预立项启动日</label>\n'
    '        <input type="date" id="start-date" class="ai-date-input"/>\n'
    '      </div>\n'
    '      <div class="ai-group">\n'
    '        <label for="target-date">预计上线日期</label>\n'
    '        <input type="date" id="target-date" class="ai-date-input"/>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="ai-output" id="ai-output">请选择预立项启动日和预计上线日期，AI 将自动生成洞察建议</div>\n'
    '  </div>\n'
    '</div>'
)

new_html = (
    '<div class="ai-insight-card">\n'
    '  <div class="ai-insight-header">\n'
    '    <div class="ai-header-left">\n'
    '      <span class="ai-icon">\U0001f916</span>\n'
    '      <span class="ai-title">AI 进度洞察</span>\n'
    '    </div>\n'
    '    <div class="ai-header-right">\n'
    '      <div class="ai-date-compact" id="date-wrap-start">\n'
    '        <input type="date" id="start-date"/>\n'
    '        <span class="ai-date-placeholder">\U0001f4c5 启动日期</span>\n'
    '      </div>\n'
    '      <div class="ai-date-compact" id="date-p-target">\n'
    '        <input type="date" id="target-date"/>\n'
    '        <span class="ai-date-placeholder">\U0001f4c5 预计上线</span>\n'
    '      </div>\n'
    '    </div>\n'
    '  </div>\n'
    '  <div class="ai-insight-body">\n'
    '    <div class="ai-output" id="ai-output"></div>\n'
    '  </div>\n'
    '</div>'
)

if old_html in content:
    content = content.replace(old_html, new_html)
    print("OK HTML structure replaced")
else:
    print("MISS HTML structure")
    idx = content.find('ai-input-row')
    print(f"  ai-input-row at: {idx}")

# 3. Phase header names
pairs = [
    ('<div class="gh-name">基建和凭证采购</div>',
     '<div class="gh-name">资源采购与申请</div>'),
    ('<div class="gh-name">信息确认</div>',
     '<div class="gh-name">信息预审与确认</div>'),
    ('<div class="gh-name">部署建设</div>',
     '<div class="gh-name">环境构建与部署</div>'),
]
for old, new in pairs:
    if old in content:
        content = content.replace(old, new)
        print(f"OK phase: {new[22:30]}")
    else:
        print(f"MISS phase: {old[22:30]}")

# 4. Legend
old_leg = '<span id="c-blocked">—</span> 已阻塞'
new_leg = '<span id="c-blocked">—</span> ❌ 阻塞'
if old_leg in content:
    content = content.replace(old_leg, new_leg)
    print("OK legend")
else:
    print("MISS legend")

# 5. META blocked label
old_meta = "blocked:  { label:'已阻塞', pill:'sp-blocked',  bar:'st-blocked'  },"
new_meta = "blocked:  { label:'❌ 阻塞', pill:'sp-blocked',  bar:'st-blocked'  },"
if old_meta in content:
    content = content.replace(old_meta, new_meta)
    print("OK META")
efe1息预审与确认', ph2:'资源采购与申请', ph3:'环境构建与部署' };"
if old_pn in content:
    content = content.replace(old_pn, new_pn)
    print("OK PHASE_NAMES")
else:
    print("MISS PHASE_NAMES")

# 7. Fix getTaskName regex
old_rx = ".replace(/待启动|进行\u4eer/mnt/saas-tob-tracker/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done. File length: {len(content)}")
