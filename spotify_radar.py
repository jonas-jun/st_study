import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from utils import load_csv, TARGET_ARTISTS, MAIN_COLS, TARGET_COLS1, TARGET_COLS2

def plot_radar_chart(data, artist_name, target_cols1):
  values = data.loc[artist_name, target_cols1].values
  categories = target_cols1
  num_vars = len(categories)

  angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
  values = np.concatenate((values, [values[0]]))
  angles += angles[:1]

  fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
  ax.fill(angles, values, color='blue', alpha=0.25)
  ax.plot(angles, values, color='blue', linewidth=2)
  ax.set_yticks([])
  ax.set_xticks(angles[:-1])
  ax.set_xticklabels(categories, fontsize=10)
  ax.set_title(f"{artist_name} Radar Chart", size=15, y=1.1)

  plt.show()
  
  
def main():
  st.title("Spotify Data Analysis 1")
  
  msg_welcome = f"""
  Spotify 데이터를 활용하여 다음 artist의 음악 스타일을 분석합니다.\n
  {TARGET_ARTISTS}
  """
  
  st.markdown(msg_welcome)
  st.divider()
  
  df = load_csv("src/filtered_spotify_dataset.csv")
  df_radar = df[MAIN_COLS + TARGET_COLS1]
  artist_avg = df_radar.groupby('artist')[TARGET_COLS1].mean()
  artist_avg_normalized = artist_avg.apply(lambda x: (x - x.min()) / (x.max() - x.min()) * 100)
  
  artist = st.text_input(
    f"다음 중에서 원하시는 artist를 입력하세요: \n{TARGET_ARTISTS}",
    "Dua Lipa",
  )
  st.divider()
  with st.spinner(f"{artist}의 radar chart를 생성합니다."):
    time.sleep(3)
    plot_radar_chart(artist_avg_normalized, artist, TARGET_COLS1)
    st.pyplot(plt, use_container_width=True)

  st.success("Success!")
  
  
if __name__ == "__main__":
  main()