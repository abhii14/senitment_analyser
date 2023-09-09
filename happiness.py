import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = glob.glob("diary/*.txt")

analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        score = analyzer.polarity_scores(content)
        positivity.append(score["pos"])
        negativity.append(score["neg"])

dates = [name.strip(".txt").strip("dairy/") for name in filepaths]

title = st.title("Dairy Tone")
subheading = st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                    labels={"x": "Dates", "y" : "Positivity"})
st.plotly_chart(pos_figure)

subheading = st.subheader("Negativity")
pos_figure = px.line(x=dates, y=negativity,
                    labels={"x": "Dates", "y" : "Negativity"})
st.plotly_chart(pos_figure)
