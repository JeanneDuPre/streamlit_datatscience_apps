# Import the required packages
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

## Set the width to the full screen
st. set_page_config(layout="wide")
# Set page title
st.title('Korpus Mehrsprachigkeit')
st.caption('Chisinau | Republik Moldau | von 2013 bis 2017 | 5981 | signs')

## C1 = Sankey Chart with Sprachverteilung im Korpus Mehrsprachigkeit DANKE!



## C4 = DONUT CHART for vorhandene Sprache
    # load data to display the datatset 'Sprachen vorhanden'
df_vorhanden = pd.read_csv('data/vorhanden.csv', sep=";")

x3 = df_vorhanden.iloc[0:9, 1] # 2010
x2 = df_vorhanden.iloc[9:18, 1] # 2014
x1 = df_vorhanden.iloc[27:36, 1] #2017
    # color
colors = ['#277da1', '#577590', '#4d908e', '#43aa8b', '#90be6d', '#f9c74f', '#f9844a', '#f8961e', '#f3722c']
fig1,ax1 = plt.subplots(figsize = (12, 14))
ax1.pie(x1,
        startangle=90, colors= colors, pctdistance=0.88, 
        # autopct = lambda p: format(p, '.1f') if p > 4 else None,
        autopct = lambda p: '{:.1f}%\n (2017)'.format(p) if p > 4 else None,
        radius=1.0, labeldistance=1.05, textprops={'ha':'center'},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the first Pie chart \n (2017)
ax1.pie(x2,
        startangle=90, colors= colors, pctdistance=0.85,
        # autopct = lambda p: format(p, '.1f') if p > 4 else None,
        autopct = lambda p: '{:.1f}%\n (2014)'.format(p) if p > 4 else None,
        radius=0.75,labeldistance=1.05, textprops={'ha':'center'},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the second Pie chart
ax1.pie(x3,
        startangle=90, colors= colors, pctdistance=0.8,
        # autopct = lambda p: format(p, '.1f') if p > 4 else None,
        autopct = lambda p: '{:.1f}%\n (2010)'.format(p) if p > 4 else None,
        radius = 0.5,labeldistance=1.05, textprops={'ha':'center'},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the third Pie chart
centre_circle = plt.Circle((0,0), 0.25, fc="white", ) 
title = "Die vorhandenen Sprachen auf den signs im Viertel \nCentru von Chisinau"
subtitle = "Von innen nach außen wurden die Daten den folgenden Inhalten entnommen:\n2010 - Muth und Wolf (2010), S.7\n2014 - Korpus Mehrsprachigkeit nur im Jahr 2014 aufgenommene signs\n2017 - Korpus Mehrsprachigkeit in den Jahren 2013 bis 2017\naufgenommene signs"
footnote = "Quelle: Wiesemann, April 2023"
ax1.text(x=0.125, y=0.90, s=title, fontname='Arial', fontweight='bold', fontsize=14, ha='left', transform=fig1.transFigure)
ax1.text(x = 0.125, y = 0.80, s = subtitle, fontname = 'Arial', fontsize = 12, ha='left', transform= fig1.transFigure)
ax1.text(x= 0.125, y=0.08, s= footnote, fontname='Arial', fontstyle='italic', fontsize=12, ha='left', transform = fig1.transFigure)
ax1.legend(labels=df_vorhanden.iloc[0:9, 0], loc="lower right")
plt.subplots_adjust(top=0.8, wspace=0.3)
plt.legend(labels=df_vorhanden.iloc[0:9, 0], loc=(1.0,0.40), fontsize=12)
fig1 = plt.gcf()
fig1.gca().add_artist(centre_circle)
plt.axis('equal')
plt.tight_layout(pad=3)
plt.show()


## C5 = DONUT CHART for dominante Sprache
    # load data to display the datatset 'Sprachen vorhanden'
df_dominant = pd.read_csv('data/dominant.csv', sep=";")

x3_2012 = df_dominant.iloc[0:4, 1] # 2012
x2_2014 = df_dominant.iloc[4:8, 1] # 2014
x1_2017 = df_dominant.iloc[12:16, 1] #2017
    ## color
colors_2 = ['#277da1', '#577590', '#f8961e', '#f3722c']

fig2,ax2 = plt.subplots(figsize = (12, 14))

    # draw the first Pie chart \n (2017)
ax2.pie(x1_2017,
        startangle=90, colors= colors_2, pctdistance=0.88, 
        # autopct= '%1.0f%%, \n (2017)',
        autopct = lambda p: '{:.1f}%\n (2017)'.format(p) if p > 4 else None,
        radius=1.0,labeldistance=1.05, textprops={'fontweight': 'normal', 'fontsize': 12},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the first Pie chart \n (2017)
ax2.pie(x2_2014,
        startangle=90, colors= colors_2, pctdistance=0.85, 
        # autopct= '%1.0f%%, \n (2014)', 
        autopct = lambda p: '{:.1f}%\n (2014)'.format(p) if p > 4 else None,
        radius=0.75,labeldistance=1.05, textprops={'fontweight': 'normal', 'fontsize': 12},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the second Pie chart
ax2.pie(x3_2012,
        startangle=90, colors= colors_2, pctdistance=0.8, 
        # autopct= '%1.0f%% \n (2010)', 
        autopct = lambda p: '{:.1f}%\n (2012)'.format(p) if p > 4 else None,
        radius=0.5,labeldistance=1.05, textprops={'fontweight': 'normal', 'fontsize': 12},
        wedgeprops = { 'linewidth': 3, 'edgecolor': 'white'}) # draw the third Pie chart
centre_circle = plt.Circle((0,0), 0.25, fc="white", ) 
title= "Die dominanten Sprachen auf den signs im Viertel Centru in Chisinau"
subtitle="Von innen nach außen wurden die Daten den folgenden Inhalten entnommen: \n    2012 - Muth (2012b), S.217\n    2014 - Korpus Mehrsprachigkeit nur im Jahr 2014 aufgenommene signs\n    2017 - Korpus Mehrsprachigkeit in den Jahren 2013 bis 2017 \n               aufgenommene signs"
footnote = "Quelle: Wiesemann, April 2023"
ax2.text(x = 0.125, y = 0.90, s = title, fontname = 'Arial', fontweight= 'bold', fontsize = 14, ha='left', transform= fig2.transFigure)
ax2.text(x = 0.125, y = 0.80, s = subtitle, fontname = 'Arial', fontsize = 12, ha='left', transform= fig2.transFigure)
ax2.text(x= 0.125, y=0.15, s= footnote, fontname='Arial', fontstyle='italic', fontsize=12, ha='left', transform = fig2.transFigure)
ax2.legend(labels=df_dominant.iloc[0:4, 0], loc="lower right")
plt.legend(labels=df_dominant.iloc[0:4, 0], loc=(1.0,0.50), fontsize=12)
fig2 = plt.gcf()
fig2.gca().add_artist(centre_circle)
plt.axis('equal')
plt.tight_layout(pad = 3)
plt.show()



## C3 
        # load data to display the dataset 'Korpus Mehrsprachigkeit'
df = pd.read_csv('data/korpusdaten_multi.csv')




# C2 = Wordcloud with Moldova Flag
image2 = Image.open('images/moldova_img_better_better.png')



# C7 = Sunkey Chart as flech for Größe der Werbeplakate and SPinsgesamt BITTE NOCH EINMAL IN DATEN SUCHEN-> NEUE TABELLE MUSS DAFÜR ERSTELLT WERDEN DANKE!
df_sp = df[(df['SPinsgesamt'] == 'Rumänisch') | (df['SPinsgesamt'] == 'Russisch')\
    | (df['SPinsgesamt'] == 'Englisch') | (df['SPinsgesamt'] == 'Rumänisch/Russisch')]
# Größe des WPs und SPinsgesamt des WPs
category_order=['A0-A1', 'A2-A3', 'A4', 'A5', '<A5']
palette_colors = {'Rumänisch': '#277da1', 'Russisch': '#577590', 'Englisch':'#f8961e', 'Rumänisch/Russisch': '#4d908e'}
# Create a countplot
fig7,ax7 = plt.subplots(figsize = (12, 14))
ax7 = sns.countplot(data = df_sp, x= 'Größe', hue='SPinsgesamt', edgecolor= 'black', order=category_order, palette= palette_colors)
# Customize the x-axis label
ax7.set_xlabel('Größe des signs')
# Customize the y-axis label
ax7.set_ylabel('Anzahl')
#Customize the legend title
ax7.legend(title='Sprache des signs')





# C7 = Wordcloud with Moldova Flag for english words
image7 = Image.open('images/moldova_promotion_engl.png')


# C6 = Wordcloud-Vergleich (Vergleich der Wörter auf russischen und auf englischen Werbeplakaten miteinander\)
# grün= auf beiden vorkommend, blau = nur auf russischen WPs vorkommend, red = nur auf englischen WPS vorkommend
image6 = Image.open('images/moldova_wordcloud_engl_ru.png')

# C8 = altair Diagramme einfügen
alt.data_transformers.disable_max_rows()
df = pd.read_csv('data/korpusdaten_multi.csv')
df['WÖrum'] = df['ÜBSPrum'] + df['FTSPrum']
df['WÖrus'] = df['ÜBSPruss'] + df['FTSPruss']
df['WÖengl'] = df['ÜBSPengl'] + df['FTSPengl']
df['WÖmold'] = df['ÜBSPmold'] + df['FTSPmold']

selection = alt.selection_multi(
   fields=['Größe'], bind='legend'
)
scatter1= alt.Chart(df).mark_circle(size=50).encode(
    x=alt.Y('WÖrum:Q', title = "Anzahl der rumänischen Wörter", scale=alt.Scale(zero=False)),
    y=alt.Y('WÖrus:Q', title = "Anzahl der russischen Wörter", scale=alt.Scale(zero=False)),
    tooltip=['SPinsgesamt'], # information to display on mouse hover
    color = 'Größe',
    opacity=alt.condition(selection, alt.value(1), alt.value(0.1))
).properties(
    height=350, width=500,
    title="Vergleich der rumänischen und russischen Wortanzahl an der Größe des Werbeplakates"
).configure_title(
    fontSize=14
).add_selection(
    selection
).interactive()

## Set the LAYOUT 
## c1 -> CREATE SANKEY 
    ## c1, c2 = st.columns([1,3])
c2, c3 = st.columns([3,1])
    ## c3, c4, c5 = st.columns(3)
c4, c5 = st.columns(2)
    # c6, c7 = st.columns([2,1])
c9, c10 = st.columns(2)
c11, c12 = st.columns(2)




with st.container():
    # c1.write("Pie Chart Korpus Mehrsprachigkeit Sprachverteilung")
    # c1.write("Hello World Graph lost")
    c2.image(image2, caption='Wordcloud aller Werbeplakate im Korpus Mehrsprachigkeit', use_column_width=True)
    c3.write("Korpus Mehrsprachigkeit")
    c3.write(df.head(20))
    
with st.container():   
    # c3.write("Korpus Mehrsprachigkeit")
    # c3.write(df.head(20))
    c4.write(fig1)
    c5.write(fig2)
    
with st.container(): 
    # c7.write("Diagramm Größe des Werbeplakates und Sprache vorhanden- BITTE EIN SANKEY DIAGRAM DARAUS MACHEN DANKE!")
    # c7.write(fig7)
    # c8.write(chart) 
    # "Wörter ro und Wörter Russisch und Größe der Werbeplakate mit slider NOCH EINEN TITEL EINFÜGEN DANKE!")
    c9.image(image7, caption="WordCloud der Wörter auf englischen Werbeplakaten", use_column_width=True)
    c10.image(image6, caption="WordCloud: Vergleich Wörter der russischen und englischen Werbeplakate (grün- auf beiden vorkommend, rot- auf englischen WPs, blau- auf russischen WPs)", use_column_width=True)
with st.container():
    c11.write(scatter1)
    c12.write("Combo chart")