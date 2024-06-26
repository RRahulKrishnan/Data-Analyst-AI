# -*- coding: utf-8 -*-
"""AICSV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15yJYrzXvyEoJkzp_D6RpRR90bwmUwQSn

#Installing Libraries PandasAI
"""

!pip install pandasai

"""#API key PandasAI"""

import os
os.environ['PANDASAI_API_KEY'] = "$2a$10$FakGkHhOMbajytLY2pSm2ugmdEcwHQ2aIQ9OGA7f6hjFEFP8TPN/m"

"""#Upload Dataset"""

import pandas as pd
from google.colab import files
from pandasai import SmartDataframe

uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

print("Dataframe:")
print(df)

"""#Smart Data frame"""

sdf = SmartDataframe(df)

"""#AI Bot Prompt"""

sdf.chat("pllot graph for publishers wrt genre")