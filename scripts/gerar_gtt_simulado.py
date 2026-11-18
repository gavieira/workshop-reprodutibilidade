# Gera a planilha SIMULADA e propositalmente desorganizada do exercício GTT
# (teste de tolerância à glicose em camundongos). Não são dados reais.
# Uso, a partir da raiz do repositório: python3 scripts/gerar_gtt_simulado.py
import random, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
random.seed(2026)
tempos=[0,15,30,60,120]
perfil={"Ctrl":[130,290,250,180,135],"HFD":[165,390,420,330,225]}
grupos=[("Ctrl","F"),("Ctrl","M"),("HFD","F"),("HFD","M")]
rows=[]; n=0
for dieta,sexo in grupos:
    for k in range(3):
        n+=1
        aid=f"C{n:02d}"
        ajuste=1.0 if sexo=="F" else 1.08
        vals=[round(p*ajuste*random.uniform(0.9,1.1)) for p in perfil[dieta]]
        rows.append((aid,f"{dieta} {sexo}",vals))
# animal excluído: falha na injeção i.p. de glicose (sem pico)
excl="C11"
for i,r in enumerate(rows):
    if r[0]==excl: rows[i]=(r[0],r[1],[171,182,176,169,174])
wb=openpyxl.Workbook(); ws=wb.active; ws.title="GTT"
bold=Font(bold=True); thin=Side(style="thin"); box=Border(top=thin,bottom=thin,left=thin,right=thin)
ws["A1"]="GTT — camundongos, 12 semanas de dieta (DADOS SIMULADOS)"
ws.merge_cells("A1:G1"); ws["A1"].font=Font(bold=True,size=12); ws["A1"].alignment=Alignment(horizontal="center")
ws["C2"]="Glicemia (mg/dL)"; ws.merge_cells("C2:G2"); ws["C2"].alignment=Alignment(horizontal="center"); ws["C2"].font=bold
hdr=["Animal","Grupo"]+[f"{t} min" for t in tempos]
for j,h in enumerate(hdr,1):
    c=ws.cell(3,j,h); c.font=bold; c.border=box
red=PatternFill("solid",fgColor="F4B6B6"); grey=PatternFill("solid",fgColor="E7E6E6")
r=4
for gi,(dieta,sexo) in enumerate(grupos):
    bloco=[x for x in rows if x[1]==f"{dieta} {sexo}"]
    for aid,g,vals in bloco:
        ws.cell(r,1,aid); ws.cell(r,2,g)
        for j,v in enumerate(vals): ws.cell(r,3+j,v)
        for j in range(1,8):
            ws.cell(r,j).border=box
            if aid==excl: ws.cell(r,j).fill=red
        r+=1
    ws.cell(r,1,"Média"); ws.cell(r,1).font=bold
    for j in range(5):
        ws.cell(r,3+j,round(sum(b[2][j] for b in bloco)/len(bloco))).font=bold
    for j in range(1,8): ws.cell(r,j).fill=grey; ws.cell(r,j).border=box
    r+=1
ws.cell(r+1,1,"Linhas em vermelho: animal excluído.")
ws.column_dimensions["A"].width=10; ws.column_dimensions["B"].width=10
for c in "CDEFG": ws.column_dimensions[c].width=10
wb.save("data/gtt_simulado.xlsx")
for x in rows: print(x)
