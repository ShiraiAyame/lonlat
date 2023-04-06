import folium
from folium.plugins import HeatMap
import pandas as pd

stations = [
  { 
    "name": "Tokyo", "lat": 35.6809591, "lon": 139.7673068
  },
  {
    "name": "Kanda", "lat": 35.69169, "lon": 139.770883
  },
  {
    "name": "Ikebukuro", "lat": 35.728926, "lon": 139.71038
  },
  {
    "name": "Shinjuku", "lat": 	35.690921, "lon": 139.700258
  }
]
df = pd.DataFrame(stations)

map = folium.Map(location=[35.6809591, 139.7673068])

# ヒートマップを地図に追加
map.add_child(HeatMap(df[["lat", "lon"]], radius=50))

# Jupyter では以下のようにオブジェクトを呼び出すと表示できる
map

# htmlに保存
map.save("tokyo.html")