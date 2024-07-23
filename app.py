import streamlit as st
import requests

st.set_page_config(
    page_title="Calorie Tracker",
    page_icon="icon.png",
    menu_items={
        "About":"""Welcome to Calorie Tracker, your go-to resource for calculating the calories you burn during your favorite sports and activities. Whether you're swimming, running, practicing yoga, or playing basketball, our easy-to-use tool helps you understand how many calories you burn. Stay fit and informed with Calorie Tracker!"""
    }
)

st.write("<h2 style='color:#FFDA03'>Calculate Your Calorie Burn for Any Activity!</h2>",unsafe_allow_html=True)

activity=st.text_input('Enter Activity Name',placeholder='swimming')

btn=st.button("Calculate Calories")
if btn:
    try:
        api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity.strip())
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
        if response.status_code == requests.codes.ok:
            data=response.json()
            if(len(data)==0):
                st.info("Activity Unavailable")
            else:
                for i in data:
                        name=i["name"]
                        calories_per_hour=i["calories_per_hour"]
                        duration_minutes=i["duration_minutes"]
                        total_calories=i["total_calories"]

                        st.write(f"<h2 style=color:lightgreen;font-size:29px;>{name}</h2>",unsafe_allow_html=True)

                        st.write(f"""<ul type='square'><li style=font-size:24px;>Calories Burn/Hour: {calories_per_hour} kcal</li>
                                <li style=font-size:24px;>Duration: {duration_minutes} minutes</li><ul>""",unsafe_allow_html=True)
    except:
         st.error("Network Error")