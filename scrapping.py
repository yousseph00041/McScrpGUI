from McScrp import mcscrp
from requests import get
sc = mcscrp()
data = get('https://www.google.com/search?source=hp&ei=0o1VXJPjM5KvgweJ4IPYBg&q=python&btnK=%D8%A8%D8%AD%D8%AB+Google%E2%80%8F&oq=python&gs_l=psy-ab.3..35i39l2j0i203l8.289.2048..2350...1.0..0.344.2075.0j2j4j2......0....1..gws-wiz.....0..0j0i131.j8hrx2vNR3s').text

tags = sc.get_tags(data)
for tag in tags:
    for dt in sc.scrp(data,tag)['txt']:
        print(dt)
