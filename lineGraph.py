import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
fig = px.line(df , x = "Country" , y = "InternetUsers" , color = "Country" , title="Per capita income")
fig.show()
