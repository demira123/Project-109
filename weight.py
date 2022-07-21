import pandas as pd
import plotly.figure_factory as pff

data=pd.read_csv("heightAndWeight.csv")
weight = data["Weight(Pounds)"].to_list()

bgraph=pff.create_distplot([weight],["Weight"],show_hist=False)

bgraph.show()