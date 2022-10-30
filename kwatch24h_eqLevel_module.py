#
# kwatch24h_eqLevel_module.py | self_made_module
#
# Made: Ri-chan041024
#


import requests

def eqlevel():
    #JSON読み取り
    eqlevel_url = 'https://kwatch-24h.net/EQLevel.json'
    eqlevel_json = requests.get(eqlevel_url).json() #リクエスト

    Eq_level = eqlevel_json["l"] #int(整数) #振動レベル
    Eq_green = eqlevel_json["g"] #int(整数) #緑
    Eq_yellow = eqlevel_json["y"] #int(整数) #黄
    Eq_red = eqlevel_json["r"] #int(整数) #赤

    if Eq_level >= 2000: #振動レベルが2000超えなら赤色
        color = 0xa00000 #赤色
    elif Eq_level >= 1000: #振動レベルが1000超えならオレンジ色
        color = 0xffaa13 #オレンジ色
    elif Eq_level >= 100: #振動レベルが100超えなら緑色
        color = 0x32b464 #緑色
    else:
        color = 0x1e1e1e #灰色
    
    return Eq_level, Eq_green, Eq_yellow, Eq_red, color#返り値: 振動レベル, 緑観測点数, 黄観測点数, 赤観測点数, Embed(Discord Bot)用の色