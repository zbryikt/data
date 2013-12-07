# -*- coding: utf-8 -*- 
import re, glob

files = glob.glob("raw/p*")

print("計劃年度,主持人,執行機關,計劃名稱,執行起迄,核定金額")
for f in files:
  lines = open(f,"r").readlines()
  count = 0
  for line in lines:
    result = re.search(r'\s+<td align="center">(\d+)</td><td align="left">\s*([^<]+)</td><td align="left">(.+?)</td><td align="left"><span id="[^"]+">計畫名稱：</span><span id="[^"]+">(.+?)</span>.+?(\d+/\d+/\d+~\d+/\d+/\d+).+?([0-9,]+)元', line)
    if not result: continue
    dollar = re.sub(",","", result.group(6))
    college_pos = result.group(3).find("大學")
    if college_pos > 1:
      college = result.group(3)[:college_pos] + "大學"
    else :
      collage = result.group(3)
    print('"%s","%s","%s","%s","%s","%s","%s"'%(result.group(1),result.group(2),college,result.group(3),result.group(4),result.group(5),dollar)) #result.group(6)))
    count+=1
  if count!=200: print("<WARN> %s 有問題"%f)
