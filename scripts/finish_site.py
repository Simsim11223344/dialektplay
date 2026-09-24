from pathlib import Path
p=Path("index.html")
s=p.read_text(encoding="utf-8")
patch=r'''
<script>
function showCompare(){active(4);page("Jämför",'<h1>Jämför dialekter</h1><div class="grid"><div class="card"><label>Område 1</label><select class="select" id="compareA">'+DIALECTS.map((d,i)=>'<option value="'+i+'">'+d[0]+'</option>').join('')+'</select></div><div class="card"><label>Område 2</label><select class="select" id="compareB">'+DIALECTS.map((d,i)=>'<option value="'+i+'" '+(i===1?"selected":"")+'>'+d[0]+'</option>').join('')+'</select></div></div><div class="card" id="comparison" style="margin-top:12px"></div>');document.getElementById("compareA").onchange=renderCompare;document.getElementById("compareB").onchange=renderCompare;renderCompare()}
function renderCompare(){let a=DIALECTS[document.getElementById("compareA").value],b=DIALECTS[document.getElementById("compareB").value];document.getElementById("comparison").innerHTML='<div class="grid"><div><span class="pill">'+a[1]+'</span><h2>'+a[0]+'</h2>'+dpAudio(DP_AUDIO[a[0]])+'</div><div><span class="pill">'+b[1]+'</span><h2>'+b[0]+'</h2>'+dpAudio(DP_AUDIO[b[0]])+'</div></div><p class="muted">Lyssna på båda DialektPlay-klippen och jämför själv.</p>'}
</script>
'''
s=s.replace("</body>",patch+"</body>")
p.write_text(s,encoding="utf-8")
