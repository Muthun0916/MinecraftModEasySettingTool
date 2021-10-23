import tqdm
import requests
import os
import zipfile
import shutil
import numpy as np
from datetime import datetime
from os.path import expanduser


def main():
    modsname="mods.zip"
    home=expanduser("~")
    path=home+"\\AppData\\Roaming\\.minecraft\\mods"
    isForge = False
    version = None
    forgename="forge-"+str(version)+"-installer.jar"

    while True:
        isForgeQ = input("Forgeをダウンロードしますか？(y/n)").lower()
        if isForgeQ[0]=="y":
            isForge = True
            break
        elif isForgeQ[0]=="n":
            break



    if isForge == True:

        while True:
            print("ダウンロードしたいForgeのバージョンを入力してください。")
            version = input("入力例:1.12.2-14.23.5.2855")
            if version is not None:
                break

        print(forgename+"をダウンロードします")
        url="https://maven.minecraftforge.net/net/minecraftforge/forge/"+version+"/"+forgename
        for i in tqdm.tqdm(range(int(1e7))):
            np.pi*np.pi
        urlData = requests.get(url).content


        with open(forgename,mode="wb") as f:
            f.write(urlData)

        print(forgename+"を確認")

    if not os.path.exists(modsname):
        print("Error : ModsFile is not in same directry.")
        print("modが入ったzipを "+modsname+" にリネームして同じ階層に配置してください。")
        input("Enterを押すと終了します...")
        return

    if not os.path.exists(path):
        os.mkdir(path)
        print("modsファイルを新規作成しました")
    else:
        isApdQ = False

        while True:

            print("すでにmodsファイルが存在しています！バックアップしますか？")
            isApd = input("※zipファイルで別途保存します(y/n)").lower()

            if isApd[0]=="y":
                isApdQ = True
                break
            elif isApd[0]=="n":
                break

        if isApdQ == True:
            print("modsファイルのバックアップを作成します")
            for i in tqdm.tqdm(range(int(1e7))):
                np.pi*np.pi
            """
            urlData = requests.get(url).content
            """
            dt = str(datetime.today()).replace(".","").replace(":","").replace("-","").replace(" ","")
            shutil.make_archive(home+"\\AppData\\Roaming\\.minecraft\\"+str(dt)+"mods","zip",path)
            print("modsファイルのバックアップを作成しました")

        shutil.rmtree(path)
        os.mkdir(path)

    with zipfile.ZipFile(modsname) as existnig_zip:
        existnig_zip.extractall(path)
        print("modsの導入に成功しました")

    input("Enterを押すと終了します...")



main()
