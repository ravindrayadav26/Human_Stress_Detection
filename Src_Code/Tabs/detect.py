# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import detect


def app(df, x, y):
    # This function create the detection page

    # Add title to the page
    st.title("Stress Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Detection of Stress Level.
            </p>
        """, unsafe_allow_html=True)

    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    gsr = st.slider("GSR Data", int(df["gsr"].min()), int(df["gsr"].max()))
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()))
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()))
    lm = st.slider("Limb Movement", float(df["lm"].min()), float(df["lm"].max()))
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()))
    rem = st.slider("Rapid Eye Movement", float(df["rem"].min()), float(df["rem"].max()))
    sh = st.slider("Sleeping Hour", float(df["sh"].min()), float(df["sh"].max()))
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()))

    # Create the list to store all the features
    features = [gsr, rr, bt, lm, bo, rem, sh, hr]

    # Create a button to detect
    if st.button("Detect"):
        # Get detection and model score
        detection, score = detect(x, y, features)
        st.info("Stress level detected...")

        # Print the output according to the detection
        if detection == 1:
            st.success("The person has low stress level 🙂")
        elif detection == 2:
            st.warning("The person has medium stress level 😐")
        elif detection == 3:
            st.error("The person has high stress level! 😞")
        elif detection == 4:
            st.error("The person has very high stress level!! 😫")
        else:
            st.success("The person is stress free and calm 😄")
