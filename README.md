# PokemonGO TSP


### Introduction
Calculate the circulation method of efficient POKESTOP at PokemonGO using Python3

このプログラムではC言語を用いてポケモンGO内にあるポケストップの効率の良い周回ルートを算出する

### Quick Start

1. Clone this repository

```
git clone git@github.com:smallptarmigan/PokemonGO_TSP.git
```

2. Run program

```
python3 main.py [data] [time]
```

* data 座標csvデータのファイル

* time 散歩時間を分で設定

### 内部処理

深さ優先探索を用いたプログラムですべてのルートから指定された時間でより多くのポケストップを周ることのできるルートを出力します。

### 実行時間

ルート探索には深さ優先探索(DFS)を使用しており、プレイ時間が長くなると処理が終わらなくなる傾向があります。

10分のお散歩コースでは0.5秒から2秒ほどかかります。

15分を超えると処理が終了するのにかなり時間がかかります。

### 注意

ポケストップは緯度経度で与えられており、距離は直線距離となるため、実際の歩行距離とは多少のずれが発生します。

