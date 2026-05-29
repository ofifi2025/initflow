import sys

filepath = '/sessions/focused-dazzling-keller/mnt/saas-tob-tracker/index.html'

with open(filepath, 'r') as f:
    content = f.read()

start = content.find('  // ═══ ASSEMBLE')
end = content.find('  output.innerHTML = html;', start)
end = content.find('\n', end) + 1

if start == -1 or end == 0:
    print("ERROR: markers not found")
    sys.exit(1)

lines = []
lines.append('  // ═══ ASSEMBLE — 三区统一左色条布局 ═══')
lines.append("  var html = '';")
lines.append("")
lines.append("  // 区域1: 进度总结")
lines.append("  var summaryBorder = bannerClass === 'red' ? '#ef4444' : (bannerClass === 'orange' ? '#f59e0b' : '#10b981');")
lines.append("  var summaryColor = bannerClass === 'red' ? '#991b1b' : (bannerClass === 'orange' ? '#92400e' : '#065f46');")
lines.append("  html += '<div style=\"background:#fafafa;border:none;border-left:4px solid ' + summaryBorder + ';border-radius:8px;padding:14px 18px;margin-bottom:16px\">';")
lines.append("  html += '<p style=\"font-size:16px;font-weight:800;margin:0;color:' + summaryColor + '\">' + bannerText + '</p>';")
lines.append("  html += '<div style=\"font-size:11px;margin-top:5px;color:#64748b\">' + bannerSub + '</div>';")
lines.append("  html += '</div>';")
lines.append("")
lines.append("  // 区域2: 根因 + 关键路径 (深红色条)")
lines.append("  if (rootCause && (bannerClass === 'red' || bannerClass === 'orange')) {")
lines.append("    var rName = getTaskName(rootCause);")
lines.append("    var rDept = TASK_DEPT[rootCause] || '相关负责人';")
lines.append("    var ds = getAllDownstream(rootCause); ds.delete(rootCause);")
lines.append("    html += '<div style=\"background:#fafafa;border:none;border-left:4px solid #dc2626;border-radius:8px;padding:14px 18px;margin-bottom:16px\">';")
lines.append("    html += '<div style=\"font-size:10px;font-weight:700;color:#dc2626;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px\">\\ud83d\\udd0d 根因定位</div>';")
lines.append("    html += '<div style=\"font-size:13p· 阻塞下游 ' + ds.size + ' 项任务 · 只要它不动，后续全部顺延</div>';")
lines.append("    html += cpHtml;")
lines.append("    html += '</div>';")
lines.append("  } else if (cpHtml) {")
lines.append("    html += cpHtml;")
lines.append("  }")
lines.append("")
lines.append("  // 区域3: 行动建议 + 飞书按钮 (蓝色条)")
lines.append("  if (rootCause && (bannerClass === 'red' || bannerClass === 'orange')) {")
lines.append("    var actName = getTaskName(rootCause);")
lines.append("    var actDept = TASK_DEPT[rootCause] || '相关负责人';")
lines.append("    var fbLabel = totalOverdueDays > 3 ? '立即预警并催办' : '发送飞书提醒';")
lines.append("    html += '<div style=\"background:#fafafa;border:none;border-left:4px solid #3370ff;border-radius:8px;padding:14px 18px;margin-bottom:16px;display:flex;align-items:flex-start;justify-content:space-between;gap:16px\">';")
lines.append("    html += '<div style=\"flex:1\">';")
lines.append("    html += '<div style=\"font-size:10px;font-weight:700;color:#1d4ed8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px\">\\ud83d\\udca1 首要行动</div>';")
lines.append("    html += '<div style=\"font-size:12px;color:#1e40af;font-weight:600\">立即联系「' + actDept + '」闭环「' + actName + '」，否则部署阶段将继续顺延。</div>';")
lines.append("    html += '</div>';")
lines.append("    html += '<div style=\"display:flex;flex-direction:column;align-items:flex-end;flex-shrink:0\">';")
lines.append("    html += '<button class=\"feishu-btn\" onclick=\"showFeishuConfirm()\">';")
lines.append("    html += '<svg viewBox=\"0 0 24 24\"><path d=\"M3 17.5L8.5 12l2 2L21 3.5V7l-10.5 11-2-2L3 21.5v-4z\"/></svg>';")
lines.append("    html += fbLabel + '</button>';")
lines.append("    html += '<span class=\"feishu-hint\">点击后将通过机器人向项目群发送进度预警</span>';")
lines.append("    html += '</div></div>';")
lines.append("  } else if (actionHtml) {")
lines.append("    html += actionHtml;")
lines.append("  }")
lines.append("")
lines.append("  output.innerHTML = html;")

new_assemble = '\n'.join(lines) + '\n'

content = content[:start] + new_assemble + content[end:]

with open(filepath, 'w') as f:
    f.write(content)

print("Patch applied successfully")
