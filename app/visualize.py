import pandas as pd
import streamlit as st
import plotly.express as px
from textblob import TextBlob


def show_results(brand_data):
    df = pd.DataFrame(brand_data)
    df['sentiment'] = df['reason'].apply(lambda x: round(TextBlob(x).sentiment.polarity, 2))

    st.subheader("📊 Brand Sentiment Chart")
    fig = px.bar(df, x='brand', y='sentiment', color='sentiment', text='sentiment')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📝 Brand Reason Summary")
    for _, row in df.iterrows():
        st.markdown(f"**{row['brand']}** — *Sentiment: `{row['sentiment']}`*")
        st.caption(row['reason'])
