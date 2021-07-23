import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
ibm = (df["weight"] / ((df["height"]/100) * 2))
ibm = np.array(ibm)
print(ibm)

ibm = np.where(ibm > 25, 1, 0)

#ibm = np.where( ibm < 25, 1, 0)
df['overweight'] = ibm.astype(int)

print(df['overweight'])
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholestorol"] = np.where((df["cholesterol"] == 1), 0, 1)
df["gluc"] = np.where((df["gluc"] == 1), 0, 1)

# df.loc[df["cholestorol"] + df["gluc"] < 2 , "cholesterol" ] = 0

# print(df["cholesterol"])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['active', 'alco', "cholesterol", 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'

    figure = sns.catplot(x= "variable", kind ="count", hue= "value", data = df_cat, col= "cardio")

    figure.set_axis_labels("variables", "total")

    fig = figure.fig

    # Do not modify the next two lines
    # fig.savefig('catplot.png')
    # return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))

    & (df['height'] <= df['height'].quantile(0.975) )

    & (df['weight'] >= df['weight'].quantile(0.025) )

    & (df['weight'] <= df['weight'].quantile(0.975) ) ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dytpe= bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10,10))

    # Draw the heatmap with 'sns.heatmap()'

    dfplot = sns.heatmap(corr, fmt=".1f", vmax= 0.26, annot_kws={'size:11'}, cmap='PRGn', annot=True, mask=mask)

    plt.show()
    # Do not modify the next two lines
    # fig.savefig('heatmap.png')
    # return fig

draw_cat_plot()

draw_heat_map()
