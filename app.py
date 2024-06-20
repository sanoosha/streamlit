import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_json("events_20181003.json")
df['ts'] = pd.to_datetime(df['event_timestamp'],unit='us')
df['hour'] = df['ts'].dt.floor('h')
df_grouped = df.groupby('hour').count().reset_index()
df_grouped = df_grouped[['hour','ts']]
df_grouped = df_grouped.rename(columns={'hour':'x', 'ts':'y'})

st.bar_chart(df_grouped)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

work = alt.Chart(df_grouped).transform_aggregate(
    creations='sum(event_timestamp)',
    groupby=['week', 'source']
).transform_joinaggregate(
    total='sum(creations)',
    groupby=['week']  
).transform_calculate(
    frac=alt.datum.creations / alt.datum.total
)
# .mark_area().encode(
#     x=alt.X('week'),
#     y=alt.Y('creations:Q'),
#     color=alt.Color('source:N'),
#     opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
#     tooltip=['week', 'creations:Q', alt.Tooltip('frac:Q', format='.0%'), 'source']
# )
# .add_selection(selection).properties(title='zello work')


if __name__ == '__main__':
    print('Hello World')