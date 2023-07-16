import streamlit as st


def main():

    st.title("Heart Disease Prediction Model")
    st.image('./img3.gif')

    st.header("Heart Disease")
    st.write("Heart disease describes a range of conditions that affect the heart. Heart diseases include:")

    st.markdown("* Blood vessel disease, such as coronary artery disease")
    st.markdown("* Irregular heartbeats (arrhythmias)")
    st.markdown("* Heart problems you're born with (congenital heart defects)")
    st.markdown("* Disease of the heart muscle")
    st.markdown("* Heart valve disease")


    col1, col2 = st.columns(2)

    # symptoms column
    with col1:
        st.subheader("Symptoms of heart disease ")

        st.markdown("* Chest pain or discomfort")
        st.markdown("* Fainting (syncope) or near fainting")
        st.markdown("* Shortness of breath")
        st.markdown("* Racing heartbeat (tachycardia)")
        st.markdown("* Slow heartbeat (bradycardia)")

    # causes column
    with col2:
        st.subheader("Causes of heart disease ")

        st.markdown("* Drug misuse")
        st.markdown("* Emotional stress")
        st.markdown("* Excessive use of alcohol or caffeine")
        st.markdown("* High blood pressure")
        st.markdown("* Smoking")



    st.subheader("Risk factors")
    st.write("Risk factors for heart disease include:")

    st.markdown("* **Age.** Growing older increases the risk of damaged and narrowed arteries and a weakened or thickened heart muscle.")
    st.markdown("* **Sex.** Men are generally at greater risk of heart disease. The risk for women increases after menopause.")
    st.markdown("* **Smoking.** If you smoke, quit. Substances in tobacco smoke damage the arteries. Heart attacks are more common in smokers than in nonsmokers. If you need help quitting, talk to your health care provider about strategies that can help.")
    st.markdown("* **Unhealthy diet.** Diets high in fat, salt, sugar and cholesterol have been linked to heart disease.")
    st.markdown("* **High cholesterol.** Having high cholesterol increases the risk of atherosclerosis. Atherosclerosis has been linked to heart attacks and strokes.")
    st.markdown("* **Stress.** Unrelieved stress may damage the arteries and worsen other risk factors for heart disease.")


    st.subheader("Prevention")
    st.write("The same lifestyle changes used to manage heart disease may also help prevent it. Try these heart-healthy tips:")

    st.markdown("* Don't smoke.")
    st.markdown("* Eat a diet that's low in salt and saturated fat.")
    st.markdown("* Exercise at least 30 minutes a day on most days of the week.")
    st.markdown("* Maintain a healthy weight.")
    st.markdown("* Reduce and manage stress.")
    st.markdown("* Control high blood pressure, high cholesterol and diabetes.")
    st.markdown("* Get good sleep. Adults should aim for 7 to 9 hours daily.")

    with open("app.css") as file:
            st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

