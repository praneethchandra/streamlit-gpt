import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def clean_data(file):
    data = pd.read_csv(file, names=range(10))
    # data = data.drop('0', axis=1)
    data.columns = data.iloc[0]
    data = data[1:]

    data['Quantity'] = data['Quantity'].astype(float)

    data['Price'] = data['Price'].str.replace('$','')
    data['Price'] = data['Price'].str.replace('(','')
    data['Price'] = data['Price'].str.replace(')','')
    data['Price'] = data['Price'].astype(float)
    data['Amount'] = data['Amount'].str.replace('(','')
    data['Amount'] = data['Amount'].str.replace('$','')
    data['Amount'] = data['Amount'].str.replace(')', '')
    data['Amount'] = data['Amount'].str.replace("'", '')
    data['Amount'] = data['Amount'].str.replace(",", '')
    data['Amount'] = data['Amount'].astype(float)
    return data[data["Trans Code"] == "CDIV"]

def main():
    st.title("Hello, World! EDA Streamlit App")

    st.header("Upload your csv data file")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file is not None:
        data = clean_data(data_file)
        st.write("Data overview:")
        st.write(data.head(50))

        st.sidebar.header("Visualizations")
        plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot"]
        selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

        if selected_plot == "Bar plot":
            x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
            hue_col = st.sidebar.selectbox("Select hue", data.columns)
            st.write("Bar plot:")
            fig, ax = plt.subplots()
            sns.barplot(x=data[x_axis], y=data[y_axis], hue=data[hue_col], ax=ax)
            ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=30))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)
        
        elif selected_plot == "Scatter plot":
            x_axis = st.sidebar.selectbox("Select x-axis", data.columns)
            y_axis = st.sidebar.selectbox("Select y-axis", data.columns)
            hue_col = st.sidebar.selectbox("Select hue", data.columns)
            st.write("Scatter plot:")
            fig, ax = plt.subplots()
            sns.scatterplot(x=data[x_axis], y=data[y_axis], hue=data[hue_col], ax=ax)
            ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=30))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

        elif selected_plot == "Histogram":
            column = st.sidebar.selectbox("Select a column", data.columns)
            bins = st.sidebar.slider("Number of bins", 5, 100, 20)
            st.write("Histogram")
            fig, ax = plt.subplots()
            sns.histplot(data[column], bins=bins, ax=ax)
            ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=30))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

        elif selected_plot == "Box plot":
            column = st.sidebar.selectbox("Select a column", data.columns)
            st.write("Box plot")
            fig, ax = plt.subplots()
            sns.boxplot(data[column], ax=ax)
            ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=30))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

if __name__ == '__main__':
    main()