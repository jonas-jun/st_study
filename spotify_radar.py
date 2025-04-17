import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_dset(path):
  rst = pd.read_csv(path)
  return rst

def plot_radar_chart(data, artist_name, target_cols1):
  values = data.loc[artist_name, target_cols1].values
  categories = target_cols1
  num_vars = len(categories)

  # 각 데이터 포인트의 각도 계산
  angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
  values = np.concatenate((values, [values[0]]))  # 닫힌 도형을 위해 첫 값 추가
  angles += angles[:1]

  # 플롯 생성
  fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
  ax.fill(angles, values, color='blue', alpha=0.25)
  ax.plot(angles, values, color='blue', linewidth=2)
  ax.set_yticks([])
  ax.set_xticks(angles[:-1])
  ax.set_xticklabels(categories, fontsize=10)
  ax.set_title(f"{artist_name} Radar Chart", size=15, y=1.1)

  plt.show()
  
  
def main():
  st.title("Spotify Data Analysis")
  target_artists = ["Ed Sheeran", "Alan Walker", "Shawn Mendes", "OneRepublic", "Maroon 5", "Charlie Puth", "Dua Lipa", "Billie Eilish"]
  main_cols = ["artist", "song", "text", "Release Date"]
  target_cols1 = ["Tempo", "Loudness (db)", "Danceability", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness"]
  target_cols2 = ["Good for Party", "Good for Work/Study", "Good for Relaxation/Meditation", "Good for Running", "Good for Driving", "Good for Morning Routine", "Good for Social Gatherings"]
  
  
  msg_welcome = f"""
  다음 artist들에 대한 Spotify 데이터를 분석합니다.
  {target_artists}
  """
  
  st.markdown(msg_welcome)
  st.divider()
  
  df = load_dset("src/filtered_spotify_dataset.csv")
  
  ## 1. radar chart
  df_radar = df[main_cols+target_cols1]
  # 각 artist별로 target_cols1에 대한 평균값 계산
  artist_avg = df_radar.groupby('artist')[target_cols1].mean()
  artist_avg_normalized = artist_avg.apply(lambda x: (x - x.min()) / (x.max() - x.min()) * 100)
  
  artist = st.text_input(
    f"다음 중에서 원하시는 artist를 입력하세요: \n{target_artists}",
    "Dua Lipa",
  )
  st.divider()
  with st.spinner(f"{artist}의 radar chart를 생성합니다."):
    plot_radar_chart(artist_avg_normalized, artist, target_cols1)
    st.pyplot(plt, use_container_width=True)
  
  
  
  
  # # 2x4 배열로 레이더 차트 시각화
  # fig, axes = plt.subplots(2, 4, figsize=(20, 10), subplot_kw=dict(polar=True))

  # # 각 artist에 대해 subplot에 데이터 표시
  # for idx, artist in enumerate(artist_avg_normalized.index):
  #   row, col = divmod(idx, 4)
  #   ax = axes[row, col]
    
  #   # 데이터 가져오기
  #   values = artist_avg_normalized.loc[artist, target_cols1].values
  #   categories = target_cols1
  #   num_vars = len(categories)

  #   # 각 데이터 포인트의 각도 계산
  #   angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
  #   values = np.concatenate((values, [values[0]]))  # 닫힌 도형을 위해 첫 값 추가
  #   angles += angles[:1]

  #   # 레이더 차트 그리기
  #   ax.fill(angles, values, color='blue', alpha=0.25)
  #   ax.plot(angles, values, color='blue', linewidth=2)
  #   ax.set_yticks([])
  #   ax.set_xticks(angles[:-1])
  #   ax.set_xticklabels(categories, fontsize=10)
  #   ax.set_title(artist, size=15, y=1.1)

  # # 레이아웃 조정
  # plt.tight_layout()
  # # plt.show()
  # st.pyplot(plt, use_container_width=True)
  
  
if __name__ == "__main__":
  main()