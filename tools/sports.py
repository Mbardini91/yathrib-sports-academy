import sys; sys.path.insert(0,'/home/claude/tools')
from rig import *
GROUND=HIPY+92
def ground(color="#DCE1E8"): return f'<rect x="0" y="{GROUND}" width="400" height="{300-GROUND}" fill="{color}"/>'
def at(x,inner,y=HIPY): return f'<g transform="translate({x},{y})">{inner}</g>'
S={}

# 1 table tennis
d=1.0; t=[0,.45,1]
P=dict(rot=[6,-10,6],hipF=-25,kneeF=35,hipB=22,kneeB=25,body_t=[(0,8),(4,8),(0,8)],
       shF=[60,-75,60],elF=[-70,-25,-70],shB=[-30,-10,-30],elB=-40)
racket=f'<g transform="rotate(-20)"><rect x="-3" y="2" width="6" height="12" rx="2" fill="{NAVY}"/><ellipse cx="0" cy="24" rx="13" ry="15" fill="{RED}"/></g>'
ball=f'<g>{trA([(345,140),(232,118),(345,140)],d,t)}<circle r="6" fill="{WHITE}" stroke="#C9CFD8"/></g>'
table=f'<rect x="230" y="170" width="170" height="14" rx="3" fill="{TEAL}"/><rect x="250" y="184" width="8" height="70" fill="{NAVY}"/><rect x="380" y="184" width="8" height="70" fill="{NAVY}"/><rect x="312" y="150" width="4" height="20" fill="{NAVY}"/><rect x="300" y="150" width="28" height="14" fill="none" stroke="{NAVY}" stroke-width="2"/>'
S["tabletennis"]=svg(ground()+table+at(150,figure(P,d,t,hand_front=racket))+ball,"لاعبة تضرب كرة تنس الطاولة")

# 2 volleyball (set)
d=1.3; t=[0,.5,1]
P=dict(hipF=[-25,0,-25],kneeF=[45,0,45],hipB=[-15,0,-15],kneeB=[40,0,40],body_t=[(0,14),(0,-6),(0,14)],
       shF=[-150,-178,-150],elF=[-60,-5,-60],shB=[-140,-172,-140],elB=[-60,-10,-60])
h0=fk_hand(P,0,base=(170,HIPY)); h1=fk_hand(P,1,base=(170,HIPY))
ball=f'<g>{trA([(h0[0]+4,h0[1]-14),(h1[0]+30,h1[1]-120),(h0[0]+4,h0[1]-14)],d,t)}<circle r="17" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/><path d="M-17 0 q17 -10 34 0 M0 -17 q-10 17 0 34" stroke="{RED}" stroke-width="3" fill="none"/></g>'
net=f'<rect x="300" y="110" width="6" height="{GROUND-110}" fill="{NAVY}"/><rect x="306" y="112" width="94" height="44" fill="none" stroke="{NAVY}" stroke-width="2"/><path d="M306 126 h94 M306 140 h94 M330 112 v44 M354 112 v44 M378 112 v44" stroke="{NAVY}" stroke-width="1"/><rect x="306" y="110" width="94" height="5" fill="{RED}"/>'
S["volleyball"]=svg(ground()+net+at(170,figure(P,d,t))+ball,"لاعبة ترفع كرة الطائرة")

# 3 football (kick)
d=1.4; t=[0,.4,.55,1]
P=dict(rot=[-4,-8,8,-4],hipF=[10,45,-55,10],kneeF=[10,70,5,10],hipB=[-5,-5,10,-5],kneeB=[5,10,10,5],
       shF=[-25,-40,45,-25],elF=-30,shB=[25,45,-55,25],elB=-30)
foot=fk=None
ballp=[(206,GROUND-13),(206,GROUND-13),(206,GROUND-13),(330,150),(400,120)]
bt=[0,.5,.55,.85,1]
ball=f'<g>{trA(ballp,d,bt,spline=False)}{opA([1,1,1,1,0],d,bt)}<g>{rotA([0,0,0,360,540],d,bt)}<circle r="13" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/><path d="M-4 -5 l8 0 l3 7 l-7 5 l-7 -5 z" fill="{NAVY}"/></g></g>'
goal=f'<path d="M330 {GROUND} V130 H400" fill="none" stroke="{WHITE}" stroke-width="7"/><path d="M336 140 H400 M336 160 H400 M336 180 H400 M336 200 H400 M336 220 H400 M350 136 V{GROUND} M370 136 V{GROUND} M390 136 V{GROUND}" stroke="#C9CFD8" stroke-width="1.5"/>'
S["football"]=svg(f'<rect x="0" y="{GROUND}" width="400" height="{300-GROUND}" fill="#3E8E6A"/>'+goal+at(150,figure(P,d,t))+ball,"لاعبة تسدد كرة القدم")

# 4 handball (jump throw)
d=1.6; t=[0,.3,.55,.75,1]
P=dict(body_t=[(0,0),(10,-34),(26,-46),(30,-10),(0,0)],rot=[0,6,-6,0,0],
       hipF=[0,-45,-20,-10,0],kneeF=[5,70,40,20,5],hipB=[0,25,15,5,0],kneeB=[5,60,50,15,5],
       shF=[10,160,-100,-60,10],elF=[-10,-40,-10,-20,-10],shB=[-15,-70,-50,-20,-15],elB=-20)
rel=fk_hand(P,2,base=(140,HIPY))
held=f'<g>{opA([1,0,1],d,[0,.55,1])}<circle cx="0" cy="12" r="12" fill="{RED}"/><path d="M-12 12 h24 M0 0 v24" stroke="#B93A20" stroke-width="2"/></g>'
fly=f'<g>{trA([(rel[0],rel[1]),(rel[0],rel[1]),(355,170),(355,170)],d,[0,.55,.8,1],spline=False)}{opA([0,1,0],d,[0,.55,.85])}<circle r="12" fill="{RED}"/></g>'
goal=f'<path d="M340 {GROUND} V140 H400" fill="none" stroke="{RED}" stroke-width="7" stroke-dasharray="12 10"/><path d="M346 150 H400 M346 170 H400 M346 190 H400 M346 210 H400 M346 230 H400 M360 146 V{GROUND} M380 146 V{GROUND}" stroke="#C9CFD8" stroke-width="1.5"/>'
S["handball"]=svg(ground(TEAL)+goal+at(140,figure(P,d,t,hand_front=held))+fly,"لاعبة تقفز وتسدد كرة اليد")

# 5 basketball (jump shot)
d=1.6; t=[0,.3,.5,.7,1]
P=dict(body_t=[(0,10),(0,-4),(0,-40),(0,-10),(0,10)],hipF=[-30,-5,0,-5,-30],kneeF=[50,10,0,10,50],hipB=[-25,-5,0,-5,-25],kneeB=[45,10,5,10,45],
       shF=[-60,-150,-175,-170,-60],elF=[-80,-70,-5,10,-80],shB=[-55,-140,-165,-150,-55],elB=[-80,-80,-20,0,-80])
rel=fk_hand(P,2,base=(130,HIPY))
held=f'<g>{opA([1,0,1],d,[0,.5,1])}<circle cx="6" cy="-10" r="15" fill="{RED}"/><path d="M-9 -10 h30 M6 -25 v30" stroke="{NAVY}" stroke-width="1.5"/></g>'
fly=f'<g>{trA([(rel[0]+6,rel[1]-10),(rel[0]+6,rel[1]-10),(250,30),(332,92),(332,92)],d,[0,.5,.68,.85,1],spline=False)}{opA([0,1,0],d,[0,.5,.9])}<circle r="15" fill="{RED}"/><path d="M-15 0 h30 M0 -15 v30" stroke="{NAVY}" stroke-width="1.5"/></g>'
hoop=f'<rect x="370" y="40" width="8" height="{GROUND-40}" fill="{NAVY}"/><rect x="352" y="48" width="18" height="60" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><rect x="310" y="96" width="44" height="5" rx="2" fill="{RED}"/><path d="M314 101 l6 26 h24 l6 -26" fill="none" stroke="#C9CFD8" stroke-width="2"/>'
S["basketball"]=svg(ground(RED)+hoop+at(130,figure(P,d,t,hand_front=held))+fly,"لاعبة تصوّب كرة السلة")

# 6 badminton (jump smash)
d=1.3; t=[0,.35,.55,1]
P=dict(body_t=[(0,0),(0,-30),(0,-36),(0,0)],rot=[0,8,-8,0],hipF=[-10,-40,-20,-10],kneeF=[10,60,40,10],hipB=[10,20,15,10],kneeB=[10,50,40,10],
       shF=[-30,165,-150,-30],elF=[-20,-60,0,-20],shB=[20,-120,-60,20],elB=-20)
racket=f'<g transform="rotate(10)"><rect x="-2" y="0" width="4" height="22" fill="{NAVY}"/><ellipse cx="0" cy="36" rx="11" ry="15" fill="none" stroke="{TEAL}" stroke-width="3"/></g>'
sh_path=[(240,40),(205,52),(196,58),(330,240),(330,240)]
shut=f'<g>{trA(sh_path,d,[0,.35,.55,.8,1],spline=False)}{opA([1,1,1,0],d,[0,.35,.8,.95])}<path d="M0 0 l-8 -12 h16 z" fill="{WHITE}" stroke="#C9CFD8"/><circle r="4" fill="{NAVY}"/></g>'
net=f'<rect x="280" y="150" width="5" height="{GROUND-150}" fill="{TEAL}"/><rect x="285" y="150" width="115" height="40" fill="none" stroke="{NAVY}" stroke-width="1.5"/><path d="M285 163 h115 M285 176 h115 M305 150 v40 M325 150 v40 M345 150 v40 M365 150 v40 M385 150 v40" stroke="{NAVY}" stroke-width=".8"/>'
S["badminton"]=svg(ground()+net+at(160,figure(P,d,t,hand_front=racket))+shut,"لاعبة تضرب الريشة الطائرة")

# 7 jump rope
d=.7; t=[0,.5,1]
P=dict(body_t=[(0,0),(0,-26),(0,0)],hipF=[0,-18,0],kneeF=[5,35,5],hipB=[0,-12,0],kneeB=[5,30,5],shF=[-25,-30,-25],elF=[-40,-50,-40],shB=[25,30,25],elB=[40,50,40])
hf=[fk_hand(P,i,True,(200,HIPY)) for i in (0,1,2)]; hb=[fk_hand(P,i,False,(200,HIPY)) for i in (0,1,2)]
def rope(i,under):
    a,b=hb[i],hf[i]; cy=GROUND+6 if under else 40
    return f"M{a[0]:.1f} {a[1]:.1f} C{a[0]-40:.1f} {cy} {b[0]+40:.1f} {cy} {b[0]:.1f} {b[1]:.1f}"
# rope: under feet at jump top (i=1), overhead when landed (i=0)
vals=";".join([rope(0,False),rope(1,True),rope(2,False)])
ropeel=f'<path fill="none" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"><animate attributeName="d" values="{vals}" keyTimes="0;0.5;1" dur="{d}s" repeatCount="indefinite"/></path>'
shadow=f'<ellipse cx="200" cy="{GROUND+4}" rx="40" ry="6" fill="#C9CFD8"><animate attributeName="rx" values="40;28;40" dur="{d}s" repeatCount="indefinite"/></ellipse>'
S["jumprope"]=svg(ground()+shadow+at(200,figure(P,d,t))+ropeel,"لاعبة تنط الحبل")

# 8 competitive fitness (squat)
d=1.8; t=[0,.5,1]
P=dict(body_t=[(0,0),(-10,40),(0,0)],hipF=[0,-85,0],kneeF=[0,100,0],hipB=[0,-80,0],kneeB=[0,95,0],waist=[0,30,0],
       shF=[-20,-95,-20],elF=[-20,0,-20],shB=[-15,-90,-15],elB=[-20,0,-20])
mat=f'<rect x="90" y="{GROUND-4}" width="220" height="10" rx="5" fill="{RED}"/>'
kb=f'<g transform="translate(330,{GROUND-26})"><path d="M-12 0 a12 12 0 1 1 24 0" fill="none" stroke="{TEAL}" stroke-width="5"/><circle cx="0" cy="12" r="16" fill="{TEAL}"/></g>'
S["fitness"]=svg(ground()+mat+kb+at(200,figure(P,d,t)),"لاعبة تؤدي تمرين القرفصاء")

# 9 athletics (run cycle)
d=.75; t=[0,.25,.5,.75,1]
P=dict(rot=-10,body_t=[(0,0),(0,-7),(0,0),(0,-7),(0,0)],hipF=[-45,0,35,10,-45],kneeF=[20,100,25,40,20],hipB=[35,10,-45,0,35],kneeB=[25,40,20,100,25],
       shF=[45,0,-45,0,45],elF=[-90,-70,-90,-70,-90],shB=[-45,0,45,0,-45],elB=[-90,-70,-90,-70,-90])
lanes=f'<rect x="0" y="{GROUND}" width="400" height="{300-GROUND}" fill="{RED}"/><path d="M0 {GROUND+18} H400 M0 {GROUND+36} H400" stroke="{WHITE}" stroke-width="3" stroke-dasharray="40 30"><animate attributeName="stroke-dashoffset" values="0;-70" dur="{d}s" repeatCount="indefinite" calcMode="linear"/></path>'
S["running"]=svg(lanes+at(190,figure(P,d,t)),"لاعبة تجري على المضمار")

# 10 chess (seated, moving a piece)
d=2.4; t=[0,.3,.55,.8,1]
P=dict(hipF=-90,kneeF=90,hipB=-85,kneeB=85,waist=[8,18,18,8,8],shF=[-20,-55,-70,-30,-20],elF=[-50,-40,-20,-60,-50],shB=-10,elB=-80)
hand=[fk_hand(P,i,True,(150,HIPY)) for i in range(5)]
knight=f'<g>{trA([(hand[0][0]+40,214),(hand[1][0]-2,hand[1][1]+4),(hand[2][0]-2,hand[2][1]+4),(hand[2][0]-2,214),(hand[0][0]+40,214)],d,t)}<path d="M-8 0 h16 l-2 -6 c2 -10 -2 -18 -10 -18 l-6 6 l4 2 l-4 6 z" fill="{NAVY}"/></g>'
board="".join(f'<rect x="{220+i*14}" y="{214}" width="14" height="6" fill="{NAVY if (i%2) else WHITE}"/>' for i in range(10))
table=f'<rect x="200" y="220" width="190" height="10" rx="3" fill="{TEAL}"/><rect x="285" y="230" width="10" height="{GROUND-230}" fill="{NAVY}"/>{board}<g transform="translate(360,196)"><rect x="-14" y="0" width="28" height="18" rx="4" fill="{RED}"/><circle cx="-6" cy="9" r="5" fill="{WHITE}"/><circle cx="6" cy="9" r="5" fill="{WHITE}"/></g>'
pieces=f'<path d="M262 214 h10 l-2 -14 h-6 z M248 214 h10 l-2 -18 h-6 z" fill="{RED}"/><path d="M318 214 h10 l-2 -16 h-6 z M334 214 h10 l-2 -12 h-6 z" fill="{NAVY}"/>'
chair=f'<rect x="96" y="{HIPY+8}" width="60" height="10" rx="4" fill="{NAVY}"/><rect x="96" y="{HIPY-60}" width="10" height="70" rx="4" fill="{NAVY}"/><rect x="104" y="{HIPY+18}" width="8" height="{GROUND-HIPY-18}" fill="{NAVY}"/>'
S["chess"]=svg(ground()+chair+table+pieces+at(150,figure(P,d,t,hijab=TEAL))+knight,"لاعبة تحرك قطعة شطرنج")

# 11 esports (seated with controller)
d=1.0; t=[0,.25,.5,.75,1]
P=dict(hipF=-90,kneeF=90,hipB=-85,kneeB=85,waist=[4,6,4,6,4],shF=[-35,-40,-33,-42,-35],elF=[-55,-50,-60,-48,-55],shB=[-30,-35,-28,-37,-30],elB=[-60,-55,-65,-52,-60],
       body_t=[(0,0),(0,-2),(0,0),(0,-2),(0,0)])
pad=f'<rect x="-4" y="-6" width="22" height="12" rx="6" fill="{NAVY}"/>'
screen=f'<rect x="250" y="70" width="140" height="96" rx="8" fill="{NAVY}"/><rect x="258" y="78" width="124" height="80" rx="4" fill="{TEAL}"/>'\
 f'<circle r="9" fill="{BLUSH}"><animate attributeName="cx" values="275;365;275" dur="{d*2}s" repeatCount="indefinite"/><animate attributeName="cy" values="140;95;140" dur="{d*2}s" repeatCount="indefinite"/></circle>'\
 f'<path d="M330 150 l14 -22 l14 22 z" fill="{RED}"><animateTransform attributeName="transform" type="translate" values="0 0;-50 0;0 0" dur="{d*3}s" repeatCount="indefinite"/></path>'\
 f'<rect x="300" y="166" width="40" height="10" fill="{NAVY}"/><rect x="270" y="176" width="100" height="{GROUND-176}" rx="4" fill="#C9CFD8"/>'
bag=f'<ellipse cx="135" cy="{HIPY+20}" rx="52" ry="22" fill="{TEAL}"/><ellipse cx="96" cy="{HIPY-10}" rx="20" ry="46" fill="{TEAL}"/>'
S["esports"]=svg(ground()+screen+bag+at(150,figure(P,d,t,hand_front=pad,top=RED))+'',"لاعبة تلعب لعبة إلكترونية")

import json
json.dump(S,open('/tmp/sports.json','w'),ensure_ascii=False)
html='<html><body style="margin:0;display:grid;grid-template-columns:repeat(4,400px);gap:6px;background:#888">'+"".join(f'<div>{v}</div>' for v in S.values())+'</body></html>'
open('/tmp/sports_preview.html','w').write(html)
print({k:len(v) for k,v in S.items()})
