import json
import os
from os.path import expanduser

def main():

    home = expanduser("~")
    memory = input("メモリを最大何GB使用しますか？")
    path=home+"\\AppData\\Roaming\\.minecraft"
    dt={}
    isDone = False


    with open(path+'\\launcher_profiles.json') as f:
        dt=json.load(f)

        for i in dt["profiles"].keys():
            if dt["profiles"][i]["name"] == "Forge":
                print("変更しました")
                dt["profiles"][i]["javaArgs"] = "-Xmx"+memory+"G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M"
                isDone=True

    if isDone == False:
        print("Forgeをインストールしてからもう一度実行してください")
        input("続けるには何かキーをおしてください")
        return

    with open(path+'\\launcher_profiles.json',"w") as of:
        json.dump(dt,of,indent=4)

    input("続けるには何かキーをおしてください")

main()
