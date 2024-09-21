import re
import argparse
import time
from rich.console import Console
from rich.progress import track

color = Console()
def ascii_art():
    color.print("""
   _______ ___     ___     _______
  / ____/ |   |___|   |   /  ___  \\
 / /      |           |  /  /___\\  \\
/ /___    |   |---|   | /   _____   \\
\____/    |___|   |___|/__/       \\__\\
    """, style='blink bold green' )
def change(file):
    with open(file,'r',encoding='utf-8') as f:
        file = open('end.txt','w',encoding='utf-8')
        for line in f.readlines():
            line = line.strip().replace(' ','').replace('\t','')
            title = re.findall(r'\d+[\.．]', line)
            for i in track(range(5), description='Processing...'):
                time.sleep(0.01)
            if title:
                num = title[0].replace('.', '').replace('．', '')
                print(f"[*]提取题号.....{num}")
                file.write(num)
                file.write('\n')
            res = re.findall(r'[A-Z][\.|．：]([\d%％\-－\u4e00-\u9fa5，（）]+)', line)
            for item in res:
                print(f"[*]提取内容.....{res}")
                file.write(item)
                file.write('\n')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='url file', required=False)
    args = parser.parse_args()
    if args.file:
        ascii_art()
        change(args.file)
        exit()



