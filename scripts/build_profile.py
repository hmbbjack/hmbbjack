from pathlib import Path
from html import escape
import json
OUT=Path(__file__).resolve().parents[1]; A=OUT/'assets'/'v2'; A.mkdir(parents=True,exist_ok=True)
C={'ink':'#123F46','muted':'#587071','cream':'#FFF9E9','yellow':'#FFE36B','aqua':'#BEEDEA','blue':'#227D98','pink':'#F4B3BA','line':'#D2E3DD'}
FONT="'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC',sans-serif"
def text(x,y,s,size=22,fill=None,weight=400,anchor='start',extra=''):
 return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill or C["ink"]}" text-anchor="{anchor}" {extra}>{escape(s)}</text>'
def rect(x,y,w,h,fill,rx=18,stroke=None,sw=1.5):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>'
def circle(x,y,r,fill,stroke=None,sw=2):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>'
def line(x1,y1,x2,y2,stroke=None,sw=2,extra=''):
 return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{stroke or C["ink"]}" stroke-width="{sw}" stroke-linecap="round" {extra}/>'
def pill(x,y,label,fill=None,width=None,fg=None):
 w=width or len(label)*18+30
 return rect(x,y,w,32,fill or C['aqua'],16)+text(x+w/2,y+22,label,16,fg,600,'middle')
def arrow(x,y,color=None):
 return f'<g stroke="{color or C["ink"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M{x} {y+11}H{x+22}M{x+14} {y+3}L{x+22} {y+11}L{x+14} {y+19}"/></g>'
def flower(x,y,scale=1,color='#53B8BD'):
 return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="2.5" opacity=".5"><path d="M0-12C-29-40-43-3-16 3C-46 20-10 43-3 17C8 48 43 23 15 9C46-2 20-36 8-14C13-45-23-43-10-15Z"/><circle r="5"/></g>'
def bubbles(x,y):
 return f'<g class="rise" fill="none" stroke="#E9FFFA" stroke-width="2">'+''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="{r}"/>' for dx,dy,r in [(0,0,10),(17,-39,5),(-10,-72,7)])+'</g>'
def jelly(x,y,s=1):
 return f'''<g transform="translate({x} {y}) scale({s})"><g class="float"><path d="M-29 0C-28-42 28-42 29 0Q0 17-29 0Z" fill="#F7BBC8" stroke="#BB768C" stroke-width="2"/><g fill="none" stroke="#BB768C" stroke-width="2" stroke-linecap="round"><path d="M-16 7Q-27 28-14 32T-14 51"/><path d="M0 10Q13 29 0 38T3 57"/><path d="M17 7Q29 22 17 30T23 47"/></g><ellipse cx="-10" cy="-12" rx="6" ry="4" fill="#E292AE"/><ellipse cx="13" cy="-15" rx="5" ry="3" fill="#E292AE"/></g></g>'''
def pineapple(x,y,s=1):
 return f'''<g transform="translate({x} {y}) scale({s})" stroke="#12525B" stroke-width="3" stroke-linejoin="round"><path d="M3-50Q-35-94-31-116Q-7-109 10-81Q3-121 19-136Q32-112 26-79Q44-111 63-111Q60-79 32-49" fill="#61B773"/><path d="M-37 2C-45-78 65-82 68 2L67 74Q15 90-37 74Z" fill="#F9BB49"/><path d="M-33-13L63 58M-22-40L66 22M-35 27L31 78M52-37L-34 29M65-1L-20 77M16-55L-37-6" stroke="#DA9639" stroke-width="2"/><path d="M-2 79V40C-2 11 37 11 37 40V79Z" fill="#6CC7CB"/><circle cx="43" cy="-4" r="13" fill="#2D92AE"/><circle cx="43" cy="-4" r="7" fill="#BCEDE7"/><path d="M5 73V42C5 23 30 23 30 42V73" fill="none"/><circle cx="25" cy="53" r="2" fill="#12525B"/></g>'''
def sponge(x,y,s=1):
 # A code-native cartoon mascot, kept deliberately crisp at GitHub profile sizes.
 return f'''<g transform="translate({x} {y}) scale({s})" stroke="#16454A" stroke-width="3.3" stroke-linecap="round" stroke-linejoin="round">
<ellipse cx="0" cy="127" rx="78" ry="12" fill="#104B53" opacity=".12" stroke="none"/>
<path d="M-62 15Q-89 3-85-20M61 13Q92-1 95-34" fill="none" stroke="#F5CE3D" stroke-width="9"/><path d="M93-33l-8-11m9 11 8-15m-6 18 17-3" stroke="#16454A" fill="none"/>
<path d="M-70-66Q-63-77-49-70Q-33-78-20-71Q-1-79 15-71Q34-78 47-69Q65-76 71-60L68 62H-69Z" fill="#FFE264"/>
<g fill="#D9B837" stroke="none"><ellipse cx="-54" cy="-51" rx="8" ry="6"/><ellipse cx="52" cy="-45" rx="6" ry="10"/><ellipse cx="-57" cy="28" rx="7" ry="5"/><ellipse cx="56" cy="29" rx="5" ry="8"/><circle cx="-11" cy="-61" r="4"/><circle cx="39" cy="55" r="4"/></g>
<ellipse cx="-24" cy="-20" rx="25" ry="29" fill="#FFFDF5"/><ellipse cx="24" cy="-20" rx="25" ry="29" fill="#FFFDF5"/>
<ellipse cx="-17" cy="-19" rx="10" ry="14" fill="#65CDE6"/><ellipse cx="17" cy="-19" rx="10" ry="14" fill="#65CDE6"/><ellipse cx="-14" cy="-18" rx="5" ry="9" fill="#16454A" stroke="none"/><ellipse cx="14" cy="-18" rx="5" ry="9" fill="#16454A" stroke="none"/>
<g stroke-width="3"><path d="M-40-42l-5-10M-25-49v-11M-10-43l3-10M10-43l-3-10M25-49v-11M40-42l5-10"/></g>
<path d="M-45 12Q0 57 45 12Q39 65 0 63Q-38 65-45 12Z" fill="#743B30"/><path d="M-15 21H-1V39H-15ZM3 21H17V39H3Z" fill="white" stroke-width="2"/>
<ellipse cx="0" cy="3" rx="10" ry="17" fill="#FFE264"/><path d="M-57 7Q-43-4-31 6M31 6Q44-4 57 7" fill="none" stroke="#E8AC2A" stroke-width="6"/>
<g fill="#E48D69" stroke="none"><circle cx="-47" cy="5" r="2"/><circle cx="-39" cy="9" r="2"/><circle cx="45" cy="4" r="2"/><circle cx="38" cy="9" r="2"/></g>
<path d="M-69 62H68V78H-69Z" fill="#FFFDF6"/><path d="M-69 78H68V99H-69Z" fill="#A76B44"/>
<path d="M-16 62 0 75 16 62M0 75-7 90 0 98 7 90Z" fill="#E66556"/>
<path d="M-35 100V116M36 100V116" stroke="#FFE264" stroke-width="7"/><path d="M-35 113V125M36 113V125" stroke="#FFFDF6" stroke-width="10"/>
<path d="M-35 126Q-67 110-70 126Q-69 133-35 132ZM36 126Q67 110 72 126Q70 133 36 132Z" fill="#16454A"/>
</g>'''
def svg(name,w,h,body,title='',anim=False):
 style='''<style>@keyframes drift{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}@keyframes up{0%,100%{transform:translateY(0);opacity:.5}50%{transform:translateY(-16px);opacity:1}}.float{animation:drift 6s ease-in-out infinite}.rise{animation:up 9s ease-in-out infinite}@media(prefers-reduced-motion:reduce){.float,.rise{animation:none}}</style>''' if anim else ''
 a=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title>{style}{body}</svg>'
 (A/name).write_text(a)
 return a
# Hero: editorial, playful, no biographical information.
for mobile in (False,True):
 w,h=(600,510) if mobile else (1000,370)
 b=rect(1,1,w-2,h-2,C['cream'],26,C['ink'],2)
 b+=line(25,59,w-25,59,C['ink'],1.4)
 b+=circle(32,31,5,'#FF8F82')+circle(50,31,5,C['yellow'])+circle(68,31,5,'#8FD5BE')
 b+=text(91,38,'比奇堡 · 个人空间',22 if mobile else 17,weight=600)
 b+=circle(w-150,31,4,'#59AE94')+text(w-134,37,'好奇心营业中',20 if mobile else 15,weight=500)
 if not mobile:
  b+=rect(630,82,344,242,C['aqua'],115)
  b+=flower(901,117,.8)+flower(651,262,.55)
  b+=pineapple(920,246,.6)+bubbles(663,196)+jelly(894,164,.47)
  b+=sponge(787,200,.88)
  b+=text(35,130,'欢迎来到',34,weight=600)
  b+=rect(30,151,489,91,C['yellow'],8)+text(36,219,'我的比奇堡',75,weight=900,extra='letter-spacing="1"')
  b+=text(36,282,'把好奇心，养成每天的小习惯。',24,weight=500)
  b+=text(36,334,'一片小海，一些想法，一点点新进步。',17,C['muted'])
  b+=text(940,345,'往下游，认识我',14,C['ink'],500,'end')
 else:
  b+=text(29,109,'欢迎来到',26,weight=600)
  b+=rect(26,128,402,73,C['yellow'],8)+text(31,184,'我的比奇堡',62,weight=900)
  b+=text(30,239,'把好奇心，养成每天的小习惯。',26,weight=500)
  b+=rect(24,271,552,213,C['aqua'],90)
  b+=flower(476,301,.65)+flower(61,428,.65)+jelly(101,340,.65)+pineapple(485,409,.65)+bubbles(416,351)
  b+=sponge(295,365,.83)
 svg('hero-mobile.svg' if mobile else 'hero.svg',w,h,b,'欢迎来到我的比奇堡，把好奇心养成每天的小习惯。',True)
# Actual linked navigation buttons.
for name,label,sub,color,num in [('nav-about.svg','居民档案','到菠萝屋坐坐',C['yellow'],'一'),('nav-projects.svg','蟹堡工坊','看看我的小工具',C['aqua'],'二'),('nav-learning.svg','水母田笔记','一起探索新东西','#F8D3D8','三')]:
 b=rect(1,1,318,82,color,17,C['ink'],1.5)+circle(31,29,13,C['cream'])+text(31,35,num,16,weight=700,anchor='middle')+text(56,35,label,25,weight=700)+text(56,62,sub,15,C['muted'])+arrow(275,31)
 svg(name,320,84,b,label+'：'+sub)
for name,label,color in [('nav-about','居民档案',C['yellow']),('nav-projects','蟹堡工坊',C['aqua']),('nav-learning','水母田笔记','#F8D3D8')]:
 b=rect(1,1,158,70,color,14,C['ink'],1.5)+text(80,45,label,24 if len(label)==4 else 22,weight=700,anchor='middle')
 svg(name+'-mobile.svg',160,72,b,label)
# Story as a resident card, with a right-hand identity rail.
for mobile in (False,True):
 w,h=(600,760) if mobile else (1000,455)
 b=rect(1,1,w-2,h-2,C['cream'],22,C['line'])
 b+=text(31,44,'一 / 居民档案',16,C['muted'],600)
 b+=text(31,94,'菠萝屋里的两张桌子',36 if not mobile else 34,weight=800)
 if not mobile:
  b+=line(680,34,680,421,C['line'],1.5)
  lines=['如果把学习生活搬到比奇堡，我的菠萝屋里会有两张桌子。','一张摊着临床医学课本，另一张亮着刚打开的代码编辑器。','','我是一名在读临床医学学生，也是编程和人工智能的新手。','遇到不懂的知识，就像追水母一样：先好奇，再慢慢弄明白。','','希望有一天，把学到的本领带进真实的临床，','让人工智能更好地帮助医生和患者。']
  for i,l in enumerate(lines): b+=text(32,148+i*29,l,19,C['ink'] if i in (0,3,6,7) else C['muted'],500 if i==3 else 400)
  b+=rect(29,390,615,39,'#E5F3E9',10)+text(47,416,'故事还在开头。今天比昨天多懂一点，就很好。',18,weight=500)
  b+=pill(713,43,'比奇堡居民证',C['yellow'],251)
  b+=circle(836,183,85,C['aqua'])+pineapple(826,190,.75)
  b+=text(836,303,'学习型居民',25,weight=700,anchor='middle')
  for j,(lab,val) in enumerate([('身份','临床医学在读'),('状态','边学边做'),('方向','医学 × 人工智能')]):
   yy=342+j*32;b+=text(713,yy,lab,16,C['muted'])+text(963,yy,val,18,weight=600,anchor='end')
 else:
  b+=pill(29,117,'临床医学在读',C['yellow'],158)+pill(198,117,'编程与人工智能新手',C['aqua'],235)
  lines=['如果把学习生活搬到比奇堡，','我的菠萝屋里会有两张桌子。','一张摊着临床医学课本，','另一张亮着刚打开的代码编辑器。','','我是一名在读临床医学学生，','也是编程和人工智能世界里的新手。','遇到不懂的知识，就像追水母一样：','先好奇，再慢慢弄明白。','','希望有一天，把本领带进真实的临床，','让人工智能更好地帮助医生和患者。']
  for i,l in enumerate(lines):b+=text(30,196+i*34,l,26,C['muted'] if i in (2,3,7,8) else C['ink'])
  b+=rect(25,650,550,85,'#E5F3E9',14)+text(45,684,'故事还在开头。',26,weight=600)+text(45,719,'今天比昨天多懂一点，就很好。',26)
 svg('about-mobile.svg' if mobile else 'about.svg',w,h,b,'居民档案：一名临床医学学生，在菠萝屋里学习编程和人工智能，希望未来把技术运用到临床。')
# Section labels, designed as strip headings rather than default Markdown rules.
def section(filename,num,title,note):
 b=rect(0,0,1000,73,'#123F46',16)+pill(19,20,num,C['yellow'],39)+text(77,48,title,29,'#FFF9E9',700)+text(973,45,note,18,'#BFE1DA',400,'end')
 svg(filename,1000,73,b,title+'。'+note)
 b=rect(0,0,600,88,'#123F46',17)+pill(20,27,num,C['yellow'],40)+text(82,58,title,35,'#FFF9E9',700)
 svg(filename.replace('.svg','-mobile.svg'),600,88,b,title+'。'+note)
section('projects-title.svg','二','蟹堡工坊','把小想法，做成能用的小工具')
section('learning-title.svg','三','水母田笔记','学习中的方向，也是下一段航程')
# Featured project is an actual full-card link to the repository.
for mobile in (False,True):
 w,h=(600,470) if mobile else (1000,306)
 b=rect(1,1,w-2,h-2,'#E1F3EE',22,C['ink'],1.8)
 b+=pill(29,24,'我的开源项目',C['yellow'],151)+text(w-29,47,'精选小工具',16,C['muted'],500,'end')
 b+=text(31,108,'论文引用小助手',39 if not mobile else 35,weight=800)
 if not mobile:
  b+=text(33,154,'让散落在论文里的引用，重新找到自己的家。',23,weight=500)
  b+=text(33,194,'扫描文档 · 转换引用 · 核对结果',19,C['muted'])
  b+=rect(30,233,202,46,C['ink'],23)+text(55,263,'打开项目仓库',19,C['cream'],600)+arrow(189,245,C['yellow'])
  b+=text(253,261,'从一个真实的小问题开始。',17,C['muted'])
  # Native vector schematic: paper -> linked citations, styled as a desk board.
  b+=rect(674,83,288,181,'#FFF9E9',20,'#8CBAB3',1.5)
  b+=rect(701,109,75,104,'#FFFFFF',8,C['ink'],1.8)+rect(858,109,75,104,'#FFE36B',8,C['ink'],1.8)
  for yy,ww in [(130,40),(146,47),(162,34),(178,42)]:b+=line(714,yy,714+ww,yy,'#82A6A5',3)
  b+=arrow(798,147)+circle(881,143,8,'none',C['ink'])+circle(908,170,8,'none',C['ink'])+line(886,150,902,164,C['ink'],2.2)
  b+=text(819,243,'从文字，到连接',16,C['muted'],500,'middle')
 else:
  b+=text(31,156,'让散落在论文里的引用，',24)+text(31,191,'重新找到自己的家。',24)
  b+=line(31,221,569,221,'#ACCCC4',1.5)
  for i,(n,t) in enumerate([('一','扫描文档'),('二','转换引用'),('三','核对结果')]):
   x=32+i*181;b+=circle(x+16,260,15,C['cream'])+text(x+16,266,n,17,weight=700,anchor='middle')+text(x+1,305,t,22,weight=600)
  b+=rect(29,357,542,75,C['ink'],18)+text(56,403,'打开项目仓库',25,C['cream'],600)+arrow(520,380,C['yellow'])
 svg('project-feature-mobile.svg' if mobile else 'project-feature.svg',w,h,b,'论文引用小助手：我的开源项目，扫描文档、转换引用、核对结果。点击打开项目仓库。')
# Exploration cards; distinct from authored work.
for filename,title,lines,bg,kind in [('project-desktop','桌面工具探索',['编程助手的使用体验，','也值得认真打磨。'],'#FFF3D5','window'),('project-agents','智能体工作台',['观察任务如何拆解，','学习工具怎样协作。'],'#E7F1FA','nodes')]:
 for mobile in (False,True):
  w,h=(300,280) if mobile else (490,225)
  b=rect(1,1,w-2,h-2,bg,20,C['line'])
  b+=pill(22,19,'派生仓库 · 学习探索','#FFFFFF',209 if not mobile else 251)
  yy=91;b+=text(22,yy,title,29 if not mobile else 27,weight=700)
  b+=text(23,yy+40,lines[0],20)+text(23,yy+70,lines[1],20)
  b+=text(23,h-24,'前往探索',18,C['muted'],500)+arrow(w-53,h-43)
  if not mobile:
   if kind=='window':
    b+=rect(365,86,93,68,'#FFFFFF',8,C['ink'],2)+line(365,105,458,105,C['ink'],2)+circle(376,96,2,C['pink'])+circle(385,96,2,C['yellow'])+text(383,138,'小工具',17,weight=600)
   else:
    b+=line(384,120,440,92,C['ink'],2)+line(384,120,439,152,C['ink'],2)+circle(383,120,15,'#FFF9E9',C['ink'])+circle(441,92,11,C['yellow'],C['ink'])+circle(440,152,11,'#B5DCD4',C['ink'])
  svg(filename+('-mobile' if mobile else '')+'.svg',w,h,b,title+'。派生仓库，学习探索。点击查看仓库。')
# Learning path (no fake percentages or implied completed milestones).
for mobile in (False,True):
 w,h=(600,515) if mobile else (1000,242)
 b=rect(1,1,w-2,h-2,C['cream'],20,C['line'])
 items=[('医学','认真打基础','临床医学在读','让每一份理解更扎实。',C['yellow']),('编程','从动手开始','从小工具练习','把重复的事情交给代码。',C['aqua']),('智能','带着问题探索','学习人工智能','期待未来与临床相遇。','#F6CED4')]
 if not mobile:
  b+=line(61,106,938,106,'#A5C6BF',2,extra='stroke-dasharray="6 7"')
  for i,(tag,title,status,desc,col) in enumerate(items):
   x=25+i*330;b+=circle(x+38,65,27,col,C['ink'],1.5)+text(x+38,72,tag,17,weight=700,anchor='middle')+text(x+79,71,title,24,weight=700)+text(x+11,133,status,22,weight=600)+text(x+11,170,desc,18,C['muted'])
  b+=text(967,214,'持续学习，没有进度条。',15,C['muted'],400,'end')
 else:
  b+=line(59,60,59,390,'#A5C6BF',2,extra='stroke-dasharray="5 7"')
  for i,(tag,title,status,desc,col) in enumerate(items):
   y=65+i*140;b+=circle(59,y,27,col,C['ink'],1.5)+text(59,y+7,tag,17,weight=700,anchor='middle')+text(109,y+3,title,29,weight=700)+text(110,y+42,status,23,weight=600)+text(110,y+74,desc,21,C['muted'])
  b+=text(567,488,'持续学习，没有进度条。',19,C['muted'],400,'end')
 svg('learning-mobile.svg' if mobile else 'learning.svg',w,h,b,'学习路线：认真学医，从动手编程开始，带着问题探索人工智能。全部仍在学习中。')
# Closing postcard with subtle drifting jellyfish.
for mobile in (False,True):
 w,h=(600,240) if mobile else (1000,155)
 b=rect(0,0,w,h,C['ink'],23)
 b+=flower(w-48,36,.85,'#397D7D')+jelly(w-105,78,.72)
 b+=text(30,58 if not mobile else 68,'学习不必一口气游完整片海。',31 if not mobile else 29,C['yellow'],700)
 b+=text(31,105 if not mobile else 116,'今天向前一点，就很好。',24,C['cream'],500)
 if mobile:b+=text(31,191,'感谢你游到这里。',20,'#BFDCD3')
 else:b+=text(676,110,'感谢你游到这里。',19,'#BFDCD3')
 svg('footer-mobile.svg' if mobile else 'footer.svg',w,h,b,'学习不必一口气游完整片海。今天向前一点，就很好。感谢你游到这里。',True)
# README uses actual anchors and links, while visual surfaces are local SVG assets.
def picture(stem,alt):
 return f'<p><picture>\n  <source media="(max-width: 767px)" srcset="assets/v2/{stem}-mobile.svg" />\n  <img src="assets/v2/{stem}.svg" width="100%" alt="{alt}" />\n</picture></p>'
r=picture('hero','欢迎来到我的比奇堡，把好奇心养成每天的小习惯。')+'\n\n'
r+='<p align="center">\n'
for name,anchor,label in [('nav-about','about','居民档案：到菠萝屋坐坐'),('nav-projects','projects','蟹堡工坊：看看我的小工具'),('nav-learning','learning','水母田笔记：一起探索新东西')]:
 r+=f'  <a href="#user-content-{anchor}"><picture><source media="(max-width: 767px)" srcset="assets/v2/{name}-mobile.svg" /><img src="assets/v2/{name}.svg" width="32%" alt="{label}" /></picture></a>\n'
r+='</p>\n\n<a name="about" id="about"></a>\n\n'+picture('about','居民档案：一名在读临床医学学生，正在学习编程与人工智能，希望将它运用到未来的临床中。')+'\n\n'
r+='''<details>
<summary>读一读我的海底小故事</summary>

如果把学习生活搬到比奇堡，我的菠萝屋里会有两张桌子：一张摊着临床医学课本，另一张亮着刚打开的代码编辑器。

我是一名**在读临床医学学生**，也是编程和人工智能世界里的新手。遇到不懂的知识，就像海绵宝宝追水母一样：先好奇，再慢慢弄明白。

我希望慢慢攒起这些本领，做出能解决真实问题的小工具。也希望有一天，把人工智能运用到未来的临床中，让技术更好地帮助医生和患者。

故事还在开头。今天比昨天多懂一点，就很好。

</details>

<a name="projects" id="projects"></a>

<img src="assets/v2/projects-title.svg" width="100%" alt="蟹堡工坊：把小想法做成能用的小工具" />

<a href="https://github.com/hmbbjack/reverse-zotero-insert">
'''+picture('project-feature','论文引用小助手：我的开源项目，扫描文档、转换引用、核对结果。点击打开项目。')+'\n</a>\n\n<p>\n'
for stem,repo,alt in [('project-desktop','cockpit-tools','桌面工具探索，派生仓库，点击查看'),('project-agents','cc-haha','智能体工作台，派生仓库，点击查看')]:
 r+=f'<a href="https://github.com/hmbbjack/{repo}"><picture><source media="(max-width: 767px)" srcset="assets/v2/{stem}-mobile.svg" /><img src="assets/v2/{stem}.svg" width="49%" alt="{alt}" /></picture></a>\n'
r+='</p>\n\n<a name="learning" id="learning"></a>\n\n<img src="assets/v2/learning-title.svg" width="100%" alt="水母田笔记：学习中的方向，也是下一段航程" />\n\n'+picture('learning','学习路线：认真打好医学基础，动手学习编程，带着问题探索人工智能。')+'\n\n'+picture('footer','学习不必一口气游完整片海。今天向前一点，就很好。')+'\n\n'
r+='''<details>
<summary>主题与素材说明</summary>

海绵宝宝主题为个人兴趣表达。角色及相关形象属于其权利方，与本账号无隶属关系。头像素材来自[海绵宝宝官方频道](https://www.youtube.com/channel/UCx27Pkk8plpiosF14qXq-VA)。本页的界面、卡片、装饰和轻动效使用可编辑的矢量图制作；开启“减少动态效果”时会停止装饰动画。

派生仓库用于学习与探索，原作者和上游项目见各仓库说明。

</details>
'''
r=r.replace('<a href="https://github.com/hmbbjack/reverse-zotero-insert">\n<p>', '<p><a href="https://github.com/hmbbjack/reverse-zotero-insert">\n').replace('</picture></p>\n</a>', '</picture>\n</a></p>')
for stem,alt in [('projects-title','蟹堡工坊：把小想法做成能用的小工具'),('learning-title','水母田笔记：学习中的方向，也是下一段航程')]:
 r=r.replace(f'<img src="assets/v2/{stem}.svg" width="100%" alt="{alt}" />',picture(stem,alt))
(OUT/'README.md').write_text(r)
# GitHub-like local review fixture, not a separately published site.
preview=r.replace('<a name="', '<a name="user-content-').replace(' id="', ' id="user-content-')
preview=preview.replace('<summary>读一读我的海底小故事</summary>','<summary>读一读我的海底小故事</summary>')
# Markdown within details remains readable for this fixture.
(OUT/'预览.html').write_text('''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>比奇堡主页设计预览</title><style>*{box-sizing:border-box}body{margin:0;background:#f6f8fa;color:#123f46;font:16px -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif}.canvas{max-width:1000px;margin:24px auto;padding:26px;border:1px solid #d1d9e0;border-radius:8px;background:#fff}.repo{margin:0 0 20px;color:#57606a;font:14px ui-monospace,monospace}img{max-width:100%;vertical-align:middle}picture{display:inline}p{margin:14px 0}details{margin:14px 0 22px;font-size:14px;color:#587071}summary{cursor:pointer}a{color:inherit}a[name]{display:block;scroll-margin-top:16px}details[open]{line-height:1.9;white-space:pre-line}@media(max-width:767px){.canvas{margin:0;padding:16px;border:0}.repo{font-size:12px}p{margin:12px 0}}</style><main class="canvas"><div class="repo">hmbbjack / README.md</div>'''+preview+'</main></html>')
print(json.dumps({'assets':len(list(A.glob('*.svg'))),'bytes':sum(p.stat().st_size for p in A.glob('*.svg'))},ensure_ascii=False))
