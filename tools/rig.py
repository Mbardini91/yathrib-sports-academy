import math
NAVY="#121B33"; RED="#D9482B"; TEAL="#1F7A8C"; BLUSH="#F7DDD6"; BG="#EEF1F5"; SKIN="#EDBE9C"; WHITE="#FFFFFF"; GOLD="#E0B04A"
HIPY=162
def ks(n): return ";".join(["0.45 0 0.55 1"]*(n-1))
def kt(n,times=None):
    if times: return ";".join(f"{t:g}" for t in times)
    return ";".join(f"{i/(n-1):.4g}" for i in range(n))
def rotA(vals,dur,times=None):
    v=";".join(f"{a:g}" for a in vals)
    return f'<animateTransform attributeName="transform" type="rotate" values="{v}" keyTimes="{kt(len(vals),times)}" calcMode="spline" keySplines="{ks(len(vals))}" dur="{dur}s" repeatCount="indefinite"/>'
def trA(vals,dur,times=None,spline=True):
    v=";".join(f"{x:g} {y:g}" for x,y in vals)
    sp=f' calcMode="spline" keySplines="{ks(len(vals))}"' if spline else ' calcMode="linear"'
    return f'<animateTransform attributeName="transform" type="translate" values="{v}" keyTimes="{kt(len(vals),times)}"{sp} dur="{dur}s" repeatCount="indefinite"/>'
def opA(vals,dur,times):
    return f'<animate attributeName="opacity" values="{";".join(str(v) for v in vals)}" keyTimes="{kt(len(vals),times)}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
def g(rot,dur,inner,times=None,static=None):
    if isinstance(rot,(list,tuple)): return f'<g>{rotA(rot,dur,times)}{inner}</g>'
    return f'<g transform="rotate({rot})">{inner}</g>'
def R(a,p):
    r=math.radians(a); x,y=p
    return (x*math.cos(r)-y*math.sin(r), x*math.sin(r)+y*math.cos(r))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def figure(P,dur,times=None,hand_front="",hand_back="",seated=False,hijab=NAVY,top=RED,pants=NAVY):
    """P: dict of joint -> list of angles (or scalar). body_t list of (x,y)."""
    def J(k,default=0): return P.get(k,default)
    leg=lambda hip,knee,front: g(J(hip),dur,
        f'<line x1="0" y1="0" x2="0" y2="44" stroke="{pants}" stroke-width="17" stroke-linecap="round"/>'
        f'<g transform="translate(0,44)">'+g(J(knee),dur,
            f'<line x1="0" y1="0" x2="0" y2="40" stroke="{pants}" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="M-6 38 h22 a6 6 0 0 1 0 12 h-22 z" fill="{RED if front else "#B93A20"}"/>',times)+'</g>',times)
    arm=lambda sh,el,front,extra: g(J(sh),dur,
        f'<line x1="0" y1="0" x2="0" y2="36" stroke="{"#EE6A4C" if front else "#B93A20"}" stroke-width="13" stroke-linecap="round"/>'
        f'<g transform="translate(0,36)">'+g(J(el),dur,
            f'<line x1="0" y1="0" x2="0" y2="30" stroke="{"#EE6A4C" if front else "#B93A20"}" stroke-width="11" stroke-linecap="round"/>'
            f'<g transform="translate(0,33)"><circle r="6" fill="{SKIN}"/>{extra}</g>',times)+'</g>',times)
    head=(f'<g transform="translate(2,-84)">'
          f'<path d="M-20 4 a20 21 0 1 1 40 0 l2 22 q-22 8 -44 0 z" fill="{hijab}"/>'
          f'<ellipse cx="6" cy="0" rx="11" ry="13" fill="{SKIN}"/><circle cx="12" cy="-2" r="2" fill="{NAVY}"/></g>')
    torso=f'<rect x="-17" y="-70" width="34" height="74" rx="15" fill="{top}"/>'
    upper=g(J("waist"),dur,
        f'<g transform="translate(0,-62)">{arm("shB","elB",False,hand_back)}</g>'+torso+head+
        f'<g transform="translate(0,-62)">{arm("shF","elF",True,hand_front)}</g>',times)
    legs=leg("hipB","kneeB",False)+f'<rect x="-15" y="-8" width="30" height="16" rx="7" fill="{pants}"/>'
    body=g(J("rot"),dur,legs+upper+leg("hipF","kneeF",True),times)
    bt=P.get("body_t")
    if bt: return f'<g>{trA(bt,dur,times)}{body}</g>'
    return body
def fk_hand(P,i,front=True,base=(0,0)):
    a=lambda k: (P.get(k,0)[i] if isinstance(P.get(k,0),(list,tuple)) else P.get(k,0))
    s,e=("shF","elF") if front else ("shB","elB")
    rb=a("rot"); w=a("waist")
    sh=R(rb+w,(0,-62)); el=add(sh,R(rb+w+a(s),(0,36))); hd=add(el,R(rb+w+a(s)+a(e),(0,33)))
    bt=P.get("body_t"); off=bt[i] if bt else (0,0)
    return add(add(hd,off),base)
def svg(scene,label):
    return f'<svg class="sport" viewBox="0 0 400 300" role="img" aria-label="{label}"><rect width="400" height="300" fill="{BG}"/>{scene}</svg>'
