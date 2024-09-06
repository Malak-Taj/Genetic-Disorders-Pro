import streamlit as st
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns

# Define color schemes 
color_schemes = {
    'Default': {
        'Yes': 'lightblue',
        'No': 'lightcoral'
    },
    'Pastel': {
        'Yes': 'lavender',
        'No': 'salmon'
    },
    'Bright': {
        'Yes': 'cyan',
        'No': 'magenta'
    }
    }
# Load the data
gene = pd.read_csv("cleaned_gene.csv")  # Load the CSV file
# gene = pd.read_pickle('gene.pkl')
st.sidebar.title("Analysis Filters")
Filters_list = ['','Common Genetic Disorder Class', 'Common Genetic Disorder SubClass','Paternal or Maternal',
                 'Gender & Disorders' , 'Birth Defects Beside Folic Acid','Birth Asphyxia Beside Birth Defects',
                 ]
category = st.sidebar.selectbox('Select Category:', Filters_list)
# Filter data based on sidebar selection
if category == Filters_list[0]:
    st.write("<p style='color:red'>Please, Select the category you are interested in (Side Bar) !</p>", unsafe_allow_html=True) 
elif category == Filters_list[1] :
    st.markdown("<span style='color:#F08080; font-size:20px;'>What Is The Most Common Genetic Disorder In Children Patients?</span>", unsafe_allow_html=True)
    # Create and display a pie chart using Plotly Express
    pie_data = gene['Genetic_Disorder'].value_counts().reset_index()
    pie_data.columns = ['Genetic_Disorder', 'Count']  # Rename columns for clarity
    fig2 = px.pie(
        pie_data,
        names='Genetic_Disorder',
        values='Count',
    )
    st.plotly_chart(fig2)
    # Additional section using a collapsible expander
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:#F08080; font-size:15px;'>
            - The Most Common Class Among Patients is Mitochondrial, Following It Single_Gene.<br>
            - Mitochondrial disorders May Be Caused By Mutation Of A Mitochondrial DNA (mtDNA) Gene Or Mutation Of A Nuclear Gene (nDNA).<br>
        </p>
        """, unsafe_allow_html=True)
        st.markdown("[Here Is A Mitochondrial Inheritance Fact Sheet !](https://www.genetics.edu.au/PDF/Mitochondrial_inheritance_fact_sheet-CGE.pdf)", unsafe_allow_html=True) 
elif category == Filters_list[2] :
    st.markdown(":") 
    st.markdown("<span style='color:#FFA500; font-size:20px;'>What Is The Common Genetic Disorder SubClass Among Children Patients ?</span>", unsafe_allow_html=True)
    classes = px.bar(gene , x ='Genetic_Disorder' , color='Disorder_Subclass')
    st.plotly_chart(classes)
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:#FFA500; font-size:15px;'>
            - Leigh Syndrome And Mitochondrial Myopathy Are The Highest Cases In Mitochondrial Disorder.<br>
            - Cystic Fibrosis And Tay Sachs The Most Frequent In Single_Gene Disorder.<br>
            - Diabetes Is The King In Multifactorial.<br>     
        </p>
        """, unsafe_allow_html=True)
elif category == Filters_list[3] :
    st.markdown("<span style='color:#ADD8E6; font-size:20px;'>Paternal or Maternal Affecting the Genetic Disorders ?</span>", unsafe_allow_html=True)
    maternal = sns.catplot(
    data=gene, y="Disorder_Subclass", hue="Maternal_gene", kind="count",
    palette="pastel", edgecolor=".6",height=4, aspect=1.5 )
    st.pyplot(maternal)
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:#F08080; font-size:15px;'>
            - Most Of Cases Inherited The Genetic Disorder From Their Mothers, Leigh Syndrome Comes On The Top.<br>
            - We Can Notice That Hemochromatosis Patients Inherited Mostly From Their Fathers.<br> 
        </p>
        """, unsafe_allow_html=True)
elif category == Filters_list[4] :
    st.markdown("<span style='color:#4682B4; font-size:20px;'>Do This Disorders Related To Specific Gender ?</span>", unsafe_allow_html=True)
    # Create the plot
    fig2, ax = plt.subplots(figsize=(3, 1.5))  # Create a figure and an axes
    sns.countplot(x='Gender', hue='Disorder_Subclass', data=gene, ax=ax)
    # Adjust the font size of the legend labels
    ax.legend(title='Disorder Subclass', fontsize=3, title_fontsize=3) 
    # Display the plot in Streamlit
    ax.tick_params(axis='y', labelsize=5)  # Adjust the y-axis label size
    ax.tick_params(axis='x', labelsize=5)  
    # Adjust the font size of the x-axis title
    ax.set_xlabel('Gender', fontsize=7)  
    ax.set_ylabel('Count' , fontsize = 7)
    st.pyplot(fig2)  # Pass the figure to st.pyplot
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:#B22222; font-size:15px;'>
            Leigh Syndrome Is At The Top In Ambigious Gender.<br>
            It Presents Equally In Males And Females As Well As The Other Subclasses.<br> 
         </p>
        """, unsafe_allow_html=True)
elif category == Filters_list[5] :
    st.markdown("<span style='color:#CD5C5C; font-size:20px;'>What Is Folic Acid Effect On The Birth Defects And Status Of The Patient?</span>", unsafe_allow_html=True)
    # Create a Sunburst plot
    fig = px.sunburst(
    gene,
    path=['Folic_acid', 'Birth_defects' ,'Status'],
    labels={'Folic_acid':'Folic Acid', 'Birth_defects':'Birth Defects', 'Status':'Status'},
    hover_data=['Status'],
    color='Folic_acid',  # Use this column to color-code the segments
    color_discrete_map = color_schemes['Pastel']
    )

    # Display the Sunburst plot in Streamlit
    st.plotly_chart(fig)
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:lavender; font-size:15px;'>
            - The Mothers Category Used Folic Acid(17,882) Is Greater Than Those Didn't Use It(13,666).<br>
            - There Were High Birth Defects, And They Were Singular Defects.<br> 
            - Deceased Patients (Their Mothers Took Folic Acid) Portion Was High.<br>
         </p>
        """, unsafe_allow_html=True)
elif category == Filters_list[6]:
    st.markdown("<span style='color:#90EE90; font-size:20px;'>Does Birth Asphyxia(Lack Of Oxygen) Affect On The Birth Defects?</span>", unsafe_allow_html=True)
    # Create a Sunburst plot
    color_map = {
        'No': '#556B2F',
        'Yes': '#90EE90',
        'No record': 'lavender'
    }
    asphyxia = px.bar(gene , x ='Birth_defects', color = 'Birth_asphyxia', color_discrete_map = color_map)
    st.plotly_chart(asphyxia)
    with st.expander("Detailed Analysis"):
        st.write("""
        <p style='color:#90EE90; font-size:15px;'>
            - Singular Defects Rate Higher Than The Multiple .<br>
            - Yes, Asphyxia Did Affect Birth Defects And Most The Patients Suffered From Asphyxia, They Suffered Birth Defects As Well.<br>
         </p>
        """, unsafe_allow_html=True)
    