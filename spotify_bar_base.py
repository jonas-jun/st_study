import streamlit as st
import time
import pandas as pd
from utils import (
    load_csv,
    get_target_artist_songs,
    TARGET_ARTISTS,
    MAIN_COLS,
    TARGET_COLS1,
    TARGET_COLS2,
)


def main():
    st.title("Spotify Data Analysis 3")

    msg_welcome = f"""
    Spotify 데이터를 활용하여 다음 artist의 음악 스타일을 분석합니다.\n
    {TARGET_ARTISTS}
    """

    st.markdown(msg_welcome)
    st.divider()

    df = load_csv("src/filtered_spotify_dataset.csv")
    artist = st.text_input(
        f"다음 중에서 원하시는 artist를 입력하세요: \n{TARGET_ARTISTS}",
        "Dua Lipa",
    )
    st.divider()

    df_bar = get_target_artist_songs(df, artist, target_cols=MAIN_COLS + TARGET_COLS2)
    with st.spinner(f"{artist}의 데이터를 counting 합니다."):
        time.sleep(2)
        cat_counts = dict()
        for cat in TARGET_COLS2:
            cat_counts[cat] = df_bar[cat].sum().item()
        result_df = pd.DataFrame(
            {"Category": list(cat_counts.keys()), "Count": list(cat_counts.values())}
        )
        result_df["Short_Category"] = result_df["Category"].map(
            {
                "Good for Party": "Party",
                "Good for Work/Study": "Work/Study",
                "Good for Relaxation/Meditation": "Relaxation",
                "Good for Running": "Running",
                "Good for Driving": "Driving",
                "Good for Morning Routine": "Morning",
                "Good for Social Gatherings": "Social",
            }
        )
        result_df["Percent"] = round(
            100 * result_df["Count"] / sum(result_df["Count"]), 1
        )
        st.dataframe(result_df, use_container_width=True)
    st.divider()

    with st.spinner(f"{artist}의 bar chart를 Streamlit 생성합니다."):
        time.sleep(2)
        st.header(f"{artist} 음악의 카테고리별 분포")
        st.bar_chart(
            data=result_df,
            x="Short_Category",
            y="Count",
            x_label="Category",
            y_label="Count",
            width=600,
            height=400,
            color="#32CD32",
            use_container_width=True,
        )

    st.success("Success!")


if __name__ == "__main__":
    main()
