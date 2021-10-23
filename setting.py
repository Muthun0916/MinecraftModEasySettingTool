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
    isMod = False
    version = ""


    while True:
        isForgeQ = input("Forgeをダウンロードしますか？(y/n)").lower()
        if len(isForgeQ)==0:
            continue
        if isForgeQ[0]=="y":
            isForge = True
            break
        elif isForgeQ[0]=="n":
            break



    if isForge == True:

        while True:
            print("ダウンロードしたいForgeのバージョンを入力してください。")
            print("入力例:1.12.2-14.23.5.2855")
            version = input()
            if len(version)!=0:
                break
        forgename="forge-"+str(version)+"-installer.jar"
        print(forgename+"をダウンロードします")
        url="https://maven.minecraftforge.net/net/minecraftforge/forge/"+version+"/"+forgename
        for i in tqdm.tqdm(range(int(1e7))):
            np.pi*np.pi
        urlData = requests.get(url).content


        with open(forgename,mode="wb") as f:
            f.write(urlData)

        print(forgename+"を確認")


    while True:
        isModQ = input("Modの導入をしますか？(y/n)").lower()
        if len(isModQ)==0:
            continue

        if isModQ[0]=="y":
            isMod=True
            break
        elif  isModQ[0]=="n":
            break

    if not os.path.exists(modsname) and isMod==True:
        print("Error : ModsFile is not in same directry.")
        print("modが入ったzipを "+modsname+" にリネームして同じ階層に配置してください。")
        input("Enterを押すと終了します...")
        return

    if not os.path.exists(path) and isMod==True:
        os.mkdir(path)
        print("modsファイルを新規作成しました")
    elif isMod==True:


        while True:

            print("すでにmodsファイルが存在しています！バックアップしますか？")
            isApd = input("※zipファイルで別途保存します(y/n)").lower()
            if len(isApd)==0:
                continue
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

    print("作業はすべて完了しました")

    input("Enterを押すと終了します...")



main()
