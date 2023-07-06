import streamlit as st
from function import upload_database, extracted_data, show_database

# ------------------------------------------setting page configuration in streamlit---------------------------------------------------------
st.set_page_config(page_title='Bizcardx Extraction', layout="wide")

#st.balloons()
st.title(':violet[Bizcardx Data Extraction🖼️]')

data_extraction, database_side = st.tabs(
    ['Data uploading and Viewing', 'Database side'])
file_name = 'thiru'
with data_extraction:
#    st.markdown(
#        "![Alt Text](https://cdn.dribbble.com/users/393235/screenshots/1643374/media/b32f920793005f554f22129c96627c56.gif)")
    st.subheader(':violet[Choose image file to extract data]')
    # ---------------------------------------------- Uploading file to streamlit app ------------------------------------------------------
    uploaded = st.file_uploader('Choose a image file')
    # --------------------------------------- Convert binary values of image to IMAGE ---------------------------------------------------
    if uploaded is not None:
        with open(f'{file_name}.png', 'wb') as f:
            f.write(uploaded.getvalue())
        # ----------------------------------------Extracting data from image (Image view)-------------------------------------------------
        st.subheader(':violet[Image view of Data]')
        if st.button('Extract Data from Image'):
            extracted = extracted_data(f'{file_name}.png')
            st.image(extracted)

        # ----------------------------------------upload data to database----------------------------------------------------------------
        st.subheader(':violet[Upload extracted to Database]')
        if st.button('Upload data'):
            upload_database(f'{file_name}.png')
            st.success('Data uploaded to Database successfully!', icon="✅")
# --------------------------------------------getting data from database and storing in df variable---------------------------------------
df = show_database()
with database_side:
#    st.markdown(
#        "![Alt Text](https://cdn.dribbble.com/users/2037413/screenshots/4144417/ar_businesscard.gif)")
    # ----------------------------------------Showing all datas in database---------------------------------------------------------------
    st.title(':violet[All Data in Database]')
    if st.button('Show All'):
        st.dataframe(df)
    # -----------------------------------------Search data in the database----------------------------------------------------------------
    st.subheader(':violet[Search Data by Column]')
    column = str(st.radio('Select column to search', ('Name', 'Designation',
                 'Company_name', 'Address', 'Contact_number', 'Mail_id', 'Website_link'), horizontal=True))
    value = str(st.selectbox('Please select value to search', df[column]))
    if st.button('Search Data'):
        st.dataframe(df[df[column] == value])
