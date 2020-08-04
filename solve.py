import os
path = "A:/blog-hexo/source/_posts"
files= os.listdir(path)
s = []
for file in files:
    if '.vscode' in file:
        continue
    if 'md' not in file:
        if (file + ".md") not in files:
            print("md is error: " + file)
        continue
    if not os.path.isdir(file):
        # if file[:-3] not in files:
            # print("dir is error: " + file)
        with open(path + "/" + file,'r', encoding='UTF-8') as r:
            lines = r.readlines()
        with open(path + "/" + file,'w', encoding='UTF-8') as w:
            flag = 0
            for l in lines:
                # if 'abbrlink' in l:
                #     continue
                if 'asset_img' in l:
                    if(not os.path.exists(path + "/" + file[:-3] + "/" + l[13:l.find("png") + 3])):
                        print(path + "/" + file[:-3] + "/" + l[13:l.find("png") + 3])
                if file[:-3] in l:
                    flag = 1
                w.write(l)
            if flag == 0:
                print("name is error: " + file)
