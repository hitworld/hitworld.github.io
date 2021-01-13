import os
path = "B:/blog-hexo/source/_posts"
files = os.listdir(path)
pngs = os.listdir("B:/blog-hexo/source/png")
s = []
png_num = 0
for file in files:
    if '.vscode' in file:
        continue
    if 'md' not in file:
        if (file + ".md") not in files:
            print("dir name is error: " + file)
        continue
    if not os.path.isdir(file):
        with open(path + "/" + file,'r', encoding='UTF-8') as r:
            lines = r.readlines()
        with open(path + "/" + file,'w', encoding='UTF-8') as w:
            flag = 0
            for l in lines:
                # if 'abbrlink' in l:
                #     continue
                if 'asset_img' in l:
                    if(not os.path.exists(path + "/" + file[:-3] + "/" + l[13:l.find("png") + 3])):
                        print("Not find " + path + "/" + file[:-3] + "/" + l[13:l.find("png") + 3])
                if '![](/png/' in l:
                    if(not os.path.exists("B:/blog-hexo/source" + l[4:-2])):
                        print("Not find B:/blog-hexo/source" + l[4:-2])
                    else:
                        if l[9:-2] in pngs:
                            pngs.remove(l[9:-2])
                if file[:-3] in l:
                    flag = 1
                w.write(l)
            if flag == 0:
                print("name is error: " + file)

print(pngs)
