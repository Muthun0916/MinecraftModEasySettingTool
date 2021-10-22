import tqdm
import requests
import os
import zipfile
import shutil
import numpy as np
from datetime import datetime
from os.path import expanduser


def main():
    forgename="forge-1.12.2-14.23.5.2855-installer.jar"
    modsname="mods.zip"
    home=expanduser("~")
    path=home+"\\AppData\\Roaming\\.minecraft\\mods"

    if not os.path.exists(forgename):
        print(forgename+"をダウンロードします")
        url="https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2855/forge-1.12.2-14.23.5.2855-installer.jar"
        for i in tqdm.tqdm(range(int(1e7))):
            np.pi*np.pi
        urlData = requests.get(url).content


        with open(forgename,mode="wb") as f:
            f.write(urlData)

    print(forgename+"を確認")

    if not os.path.exists(modsname):
        print("https://drive.google.com/drive/folders/1t59L1wWUyg7aihSYvY1ok1IuYMCUUJ-j"+\
        "からダウンロードしたzipを "+modsname+" にリネームして同じ階層に配置してください。")
        input("続けるには何かキーをおしてください")
        return

    if not os.path.exists(path):
        os.mkdir(path)
        print("modsファイルを新規作成しました")
    else:
        print("modsファイルのバックアップを作成します")
        dt = str(datetime.today()).replace(".","").replace(":","").replace("-","").replace(" ","")
        shutil.make_archive(home+"\\AppData\\Roaming\\.minecraft\\"+str(dt)+"mods","zip",path)
        print("modsファイルのバックアップを作成しました")
        shutil.rmtree(path)
        os.mkdir(path)

    with zipfile.ZipFile(modsname) as existnig_zip:
        existnig_zip.extractall(path)
        print("modsの導入に成功しました")

    input("続けるには何かキーをおしてください")



main()
