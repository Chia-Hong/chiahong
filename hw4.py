import re
from datetime import datetime
from pprint import pprint

text = '''2004 Indian Ocean earthquake and tsunami: December 26, 2004
2010 Haiti earthquake: January 12, 2010
2008 Sichuan earthquake: May 12, 2008
2005 Kashmir earthquake: October 8, 2005
2003 Bam earthquake: December 26, 2003
2011 Tōhoku earthquake and tsunami: March 11, 2011
2001 Gujarat earthquake: January 26, 2001
2015 Nepal earthquake: April 25, 2015
2006 Yogyakarta earthquake: May 26, 2006
2018 Sulawesi earthquake and tsunami: September 28, 2018
2010 Yushu earthquake: April 13, 2010
2003 Boumerdès earthquake: May 21, 2003
2005 Nias-Simeulue earthquake: March 28, 2005
2009 Sumatra earthquake: September 30, 2009
2002 Hindu Kush earthquakes: March 25, 2002'''

reg = r'\d{4}(.*)earthquake.*: (.*$)'

report = []

a = text.split('\n')
print(a)

for i in a:
    
    p = re.compile(reg)
    place = p.search(i).group(1)
    time = p.search(i).group(2)

    time_dt = datetime.strptime(time,'%B %d, %Y')
    time_output = datetime.strftime(time_dt,'%Y/%m/%d')
    
    report.append((place,time_output))

report_sorted = sorted(report,key=lambda tup :tup[1])
pprint(report_sorted)