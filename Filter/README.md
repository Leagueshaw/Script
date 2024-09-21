## README

### 前言

要想从文本中选出所有的选项，就要考虑到所有的可能

那么就有一下几种选择，是用一条正则，还是用不用的正则

```python
    f2 = f.read()
    f2 = f2.replace(' ','')
    f2 = f2.replace('\t','')
    print(f2)
    res = re.findall(r'([A-Z]\.[\u4e00-\u9fa5]+)[，；。\n]',f2)
```

如果一开始就把所有的换行符和制表符都去掉，

那么就要用正则一次匹配干净。虽然看起来很方便，但是不方便后期更改，

所以我选择从头再来，用行的形式来爬选项

```python
for line in f.readlines():
```

### 题号

一开始是想设个count，只要找到一个内容就加一

但是事实上不同的行可能只是一个题目，那么就容易让count的值超过真正的题号

所以这里需要两个正则，一个匹配题号，一个匹配选择内容

```python
title = re.findall(r'\d+[\.．]', line)
if title:
    num = title[0].replace('.', '').replace('．', '')
    print(f"[*]提取题号.....{num}")
    file.write(num)
    file.write('\n')
```

### 内容

```python
res = re.findall(r'[A-Z][\.|．：]([\d%％\-－\u4e00-\u9fa5，（）]+)', line)
for item in res:
    print(f"[*]提取内容.....{res}")
    file.write(item)
    file.write('\n')
```

### 编码

这里就是最需要强调的地方

#### 第一种：中英文不同

其中，, 和 ，的编码在Unicode中是不一样的

#### 第二种：底层编码不同

有些东西在记事本看起来是一样的，但是实际上在编码中还是有区别

例如，"%" 和 ”％“

看起来很像，但是并不是一个东西

有时候正则匹配不到可能就是因为只是看起来像
