# import libraries
import streamlit as st 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# title & subheader
st.title("Data Analysis Web App")
st.subheader("Data Analysis for CSV datasets using Python and Streamlit")


# allow users to upload datasets
upload = st.file_uploader("Upload your Dataset (in CSV format)")
if upload is not None:
    data = pd.read_csv(upload)
    
    
# show dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())


# Check datatype of each column
if upload is not None: 
    if st.checkbox("DataType of each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)


# Check Shape of the Dataset (no of rows & columns)
if upload is not None:
    data_shape = st.radio("What Dimention do you want to check?", ('Rows', 'Columns'))
    
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
        
        
# Check for NULL values in the dataset
if upload is not None:
    if st.checkbox("Check for Missing Values"):
        if data.isnull().values.any():  # Check if any null values exist
            st.warning("This dataset contains missing values.")
            
            # Display rows with missing values
            missing_rows = data[data.isnull().any(axis=1)]
            st.text("Rows with Missing Values:")
            st.dataframe(missing_rows)
            st.text(f"Number of Rows with Missing Values: {missing_rows.shape[0]}")
        else:
            st.success("Congratulations! No missing values!")
    
    
# Check for Duplicates in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Some Duplicated Values")
        # Display Duplicated Values
        duplicates = data[data.duplicated(keep=False)]
        st.write("Duplicate Rows:")
        st.dataframe(duplicates)
        
        dup = st.selectbox("Do you want to remove these duplicated values?" \
            ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are REmoved")
        if dup == "No":
            st.text("Ok, no action performed")


# Get overall statistics of the dataset
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all'))


# Enable Data Filtering
# allow users to filter data based on specific criteria
# display rows based on column values
if upload is not None:
    st.subheader("Filter Data")
    filter_col = st.selectbox("Select column to filter by:", data.columns)
    unique_values = data[filter_col].unique()
    selected_value = st.selectbox("Select value:", unique_values)
    filtered_data = data[data[filter_col] == selected_value]
    st.write("Filtered Data")
    st.write(filtered_data)
    

# Add Graphs and Visualizations
if upload is not None:
    st.subheader("Data Visualizations")
    
    # Bar chart
    if st.checkbox("Bar Chart"):
        st.write("Select columns for the bar chart:")
        x_col = st.selectbox("Select X-axis column:", data.columns, key="bar_x")
        y_col = st.selectbox("Select Y-axis column:", data.columns, key="bar_y")

        # Check if the selected columns are compatible
        try:
            if data[x_col].dtype == 'object' or data[x_col].nunique() < 20:  # X-axis should be categorical or have limited unique values
                if pd.api.types.is_numeric_dtype(data[y_col]):  # Y-axis must be numeric
                    fig, ax = plt.subplots(figsize=(8, 5))
                    sns.barplot(x=data[x_col], y=data[y_col], ax=ax)
                    ax.set_title("Bar Chart")
                    ax.set_xlabel(x_col)
                    ax.set_ylabel(y_col)
                    st.pyplot(fig)
                else:
                    st.error("The Y-axis column must contain numeric data for a bar chart.")
            else:
                st.error("The X-axis column must be categorical or have fewer than 20 unique values.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Scatter plot
    if st.checkbox("Scatter Plot"):
        x_col = st.selectbox("Select X-axis column:", data.columns)
        y_col = st.selectbox("Select Y-axis column:", data.columns)
        sns.scatterplot(x=data[x_col], y=data[y_col])
        st.pyplot()
    
    # Histogram
    if st.checkbox("Histogram"):
        hist_col = st.selectbox("Select column for histogram:", data.columns)
        bins = st.slider("Select number of bins:", min_value=5, max_value=50, value=10)
        sns.histplot(data[hist_col], bins=bins)
        st.pyplot()
    
    # Correlation Heatmap
    if st.checkbox("Correlation Heatmap"):
        st.write("Correlation Heatmap of Numerical Features")
        sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
        st.pyplot()


# About Selection
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Quick Data Analysis of your Dataset")