import re



with open('res.txt', 'r', encoding='utf-8') as f:
    file = open('end.txt', 'w', encoding='utf-8')
    for line in f.readlines():
        line = line.strip().replace(' ', '').replace('\t', '')
        title = re.findall(r'\d+[\.．]',line)
        if title:
            num = title[0].replace('.','').replace('．','')
            file.write(num)
            file.write('\n')
        res = re.findall(r'[A-Z][\.|．：]([\d%％\-－\u4e00-\u9fa5，（）]+)', line)
        for item in res:
            file.write(item)
            file.write('\n')