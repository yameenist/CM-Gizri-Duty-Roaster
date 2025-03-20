import streamlit as st
import pandas as pd

# ✅ Set up page config
st.set_page_config(page_title="CM Gizri Roster", layout="wide")

# ✅ Load Data Function
def load_data():
    data = [
        {
            "Supervisor": "ZAHID HUSSAIN",
            "Emp#": "80023543",
            "Task": "CM",
            "Lineman": "M.YASIR",
            "Lineman_Emp#": "80022006",
            "Fitter": "MUHAMMAD FAHIM",
            "Fitter_Emp#": "80023263",
            "Karkun": "MIRZA FAIZAN",
            "Karkun_Emp#": "1170",
            "Off_Day": "Sun",
            "Duty_Time": "M,M,M,M Mon-Sat"
        },
  {
    "Supervisor": "M.IRFAN ARAIN",
    "Emp#":" 80023407",
    "Task": "CM",
    "Lineman": "MUHAMMAD NASIR ALI",
    "Lineman_Emp#": "80022310",
    "Fitter": "IMRAN ALI",
    "Fitter_Emp#": "80022216",
    "Karkun": "ARSHAD",
    "Karkun_Emp#": "SE-7121",
    "Off_Day": "Tue",
    "Duty_Time":"M,M,M,M Wed-Mon"
  },
  {
    "Supervisor": "RIASAT ALI",
    "Emp#": "4599",
    "Task": "CM",
    "Lineman": "ATTA MOHAMMAD BALOCH",
    "Lineman_Emp#": "14541",
    "Fitter": "JUNAID",
    "Fitter_Emp#": "80022260",
    "Karkun": "BABOO HAROON",
    "Karkun_Emp#": "11993",
    "Off_Day": "Fri",
    "Duty_Time":"M,M,M,M Sat-Thu"
  },
  {
    "Supervisor": "WASEEM-UR-REHMAN",
    "Emp#": "80023743",
    "Task": "CM",
    "Lineman": "ARIF HUSSAIN",
    "Lineman_Emp#": "80022463",
    "Fitter": "VACANT",
    "Karkun": "SAJJAD",
    "Karkun_Emp#": "HK-574",
    "Off_Day": "Mon",
    "Duty_Time":"M,M,M,M Tue-Sun"
  },
  {
    "Supervisor": "AKHTAR HUSSAIN",
    "Emp#":" 8970",
    "Task": "CM",
    "Lineman": "MUHAMMAD ASIF",
    "Lineman_Emp#": "80022304",
    "Fitter": "NAZEER AHMED",
    "Fitter_Emp#": "80022037",
    "Karkun": "MUHAMMAD SHAHID",
    "Karkun_Emp#":" 6598",
    "Off_Day": "Sun",
    "Duty_Time":"N,N,N,N Mon-Sat"
  },

  {
    "Supervisor": "SHAZAIB AHMED",
    "Emp#": "80023818",
    "Task": "CM",
    "Lineman": "YASIR KHAN",
    "Lineman_Emp#": "80021985",
    "Fitter": "SHAHNAWAZ",
    "Fitter_Emp#": "80022870",
    "Karkun": "ARSHAD",
    "Karkun_Emp#": "P-0056",
    "Off_Day": "Fri",
    "Duty_Time":"E,E,E,E Sat-Thu"
  },
  {
    "Supervisor": "SHEHZAD AHMED",
    "Emp#": "80023729",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#": "80022173",
    "Fitter": "MOHAMMAD ASIM",
    "Fitter_Emp#":" 5726",
    "Karkun": "MUHAMMAD LUQMAN",
    "Karkun_Emp#": "P-1913",
    "Off_Day": "Fri",
    "Duty_Time":"N,N,M,M,M Sat-Thu"
  },
  {
    "Supervisor": "MUHAMMAD ZEESHAN",
    "Emp#": "80023745",
    "Task": "CM",
    "Lineman": "NOMAN AHMED",
    "Lineman_Emp#": "80022548",
    "Fitter": "MUHAMMAD ADIL BHATI",
    "Fitter_Emp#": "80022286",
    "Karkun": "DANISH AHMED",
    "Karkun_Emp#": "MM-6598",
    "Off_Day": "Sun",
    "Duty_Time":"E,E,N,N Mon-Sat"
  }
  ,
  {
    "Supervisor": "WAJID SOMROO",
    "Emp#": "80018698",
    "Task": "CM",
    "Lineman": "MUHMMAD NADEEM",
    "Lineman_Emp#": "14316",
    "Fitter": "WAQAR AHMED",
    "Fitter_Emp#":" 10801",
    "Karkun": "IMRAN KHAN",
    "Karkun_Emp#": "0652",
    "Off_Day": "Wed",
    "Duty_Time":"N,E,N,E Thu-Tue"
  },
  {
    "Supervisor": "MASOOD ALI",
    "Emp#": "80025132",
    "Task": "CM",
    "Lineman": "NASEEM ANJUM",
    "Lineman_Emp#": "80023135",
    "Fitter": "VACANT",
    "Karkun": "QADIR BUX",
    "Karkun_Emp#": "P-0892",
    "Off_Day": "Sat",
    "Duty_Time":"N,E,N,M Mon-Fri"
  },
  {
    "Supervisor": "ALI REHAN",
    "Emp#":" 80023733",
    "Task": "CM",
    "Lineman": "ABDUL HAMEED BALOCH",
    "Lineman_Emp#": "80022318",
    "Fitter": "ABDUL QADIR",
    "Fitter_Emp#": "80022283",
    "Karkun": "SUALEH KHAN",
    "Karkun_Emp#": "P-1934",
    "Off_Day": "Sun",
    "Duty_Time":"M,M,E,E Mon-Sat"
  }
  ,
  {
    "Supervisor": "MUHAMMAD NASIR",
    "Emp#": "80023438",
    "Task": "CM",
    "Lineman": "SHAHZAD ABBASI",
    "Lineman_Emp#": "80022442",
    "Fitter": "MUHAMMAD FAIZ",
    "Fitter_Emp#": "80023269",
    "Karkun": "MUHAMMAD LAIQ",
    "Karkun_Emp#": "P-1942",
    "Off_Day": "Mon",
    "Duty_Time":"N,N,M,M Tue-Sun"
  }
  ,
  {
    "Supervisor": "M.ANUS",
    "Emp#": "80023960",
    "Task": "CM",
    "Lineman": "FARHAN KHAN",
    "Lineman_Emp#": "80022281",
    "Fitter": "AQIL AHMED",
    "Fitter_Emp#": "80023039",
    "Karkun": "KASHIF AHMAD KHAN",
    "Karkun_Emp#": "HK-716",
    "Off_Day": "Wed",
    "Duty_Time":"E,E,E,E Thu-Tue"
  }
  ,
  {
    "Supervisor": "DIYAR GUL",
    "Emp#":" 80023098",
    "Task": "CM",
    "Lineman": "MUSLIM",
    "Lineman_Emp#": "80023758",
    "Fitter": "VACANT",
    "Karkun": "MOHAMMAD ATIF",
    "Karkun_Emp#": "C-2850",
    "Off_Day": "Tue",
    "Duty_Time":"E,N,E,E Wed-Mon"
  },
  {
    "Supervisor": "MUHAMMAD YAMEEN",
    "Emp#":" 80018664",
    "Task": "CM",
    "Lineman": "CHANZAIB",
    "Lineman_Emp#": "11917",
    "Fitter": "FAROOQ",
    "Fitter_Emp#": "80023268",
    "Karkun": "IRFAN AHMED KHAN",
    "Karkun_Emp#": "C-2835",
    "Off_Day": "Thu",
    "Duty_Time":"M,E,E,N Fri-Wed"
  },
  {
    "Supervisor": "SHABBER",
    "Emp#":" 80023546",
    "Task": "CM",
    "Lineman": "MUQARRAM SHAH",
    "Lineman_Emp#":" 8698",
    "Fitter": "VACANT",
    "Karkun": "FARAZ",
    "Karkun_Emp#": "SE-7123",
    "Off_Day": "Sun",
    "Duty_Time":"E,N,E,N Mon-Sat",
  },
  {
    "Supervisor": "ALTAF",
    "Emp#": "12592",
    "Task": "CM",
    "Lineman": "SARDAR",
    "Lineman_Emp#": "80023763",
    "Fitter": "SYED ZAMEER SHAH",
    "Fitter_Emp#": "15215",
    "Karkun": "KHALID",
    "Karkun_Emp#": "C-2894",
    "Off_Day": "Sun",
    "Duty_Time":"N,E,N,E Mon-Sat"
  },
  {
    "Supervisor": "MANSOOB",
    "Emp#": "80025358",
    "Task": "GIS",
    "Lineman": "-",
    "Fitter": "-",
    "Karkun": "-",
    "Off_Day": "Sun",
    "Duty_Time":"M,M,M,M Mon-Sat",
  },
  {
    "Supervisor": "NOMAN",
    "Emp#": "80010300",
    "Task": "SI MAINT",
    "Lineman": "-",
    "Fitter": "-",
    "Karkun": "-",
    "Off_Day": "",
    "Duty_Time":"",
  },
  {
    "Supervisor": "NADEEM SARWAR",
    "Emp#": "80024426",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#": "80022618",
    "Fitter": "IMRAN BALOCH",
    "Fitter_Emp#": "80022614",
    "Karkun": "ARIF HUSSAIN",
    "Karkun_Emp#": "1157",
    "Off_Day": "Thu",
    "Duty_Time":"E,N,M,E Fri-Wed",
  },
  {
    "Supervisor": "ZEESHAN SHAIKH",
    "Emp#": "80010182",
    "Task": "CM",
    "Lineman": "M. SULEMAN",
    "Lineman_Emp#": "11081",
    "Fitter": "MUHAMMAD ASHFAQ",
    "Fitter_Emp#": "80022868",
    "Karkun": "MUHAMMAD KAMRAN",
    "Karkun_Emp#": "MMA-4693",
    "Off_Day": "Wed",
    "Duty_Time":"M,M,E,E Thu-Tue",
  },
  {
    "Supervisor": "NABEEL",
    "Emp#":" 14684",
    "Task": "CM",
    "Lineman": "M. SIRAJ",
    "Lineman_Emp#": "80023649",
    "Fitter": "ZAFAR IQBAL",
    "Fitter_Emp#":" 80023286",
    "Karkun": "JOHN",
    "Karkun_Emp#": "241",
    "Off_Day": "Sat",
    "Duty_Time":"E,M,E,N Sun-Fri",
  },
  {
    "Supervisor": "ALFRED YOUSAF",
    "Emp#": "80014989",
    "Task": "CM",
    "Lineman": "ZUBAIR ASLAM",
    "Lineman_Emp#": "80021850",
    "Fitter": "MUHAMMAD ADNAN",
    "Fitter_Emp#": "80022285",
    "Karkun": "VISHAL MUNAWAR",
    "Karkun_Emp#": "F-KE-0605",
    "Off_Day": "Mon",
    "Duty_Time":"E,E,N,N Tue-Sun",
  },
  {
    "Supervisor": "IMRAN KHAN",
    "Emp#":" 80023400",
    "Task": "CM",
    "Lineman": "AKBER HUSSAIN",
    "Lineman_Emp#":" 80022050",
    "Fitter": "SAMEER",
    "Fitter_Emp#":" 80021732",
    "Karkun": "UMER FAROOQ",
    "Karkun_Emp#":" 7997",
    "Off_Day": "Sat",
    "Duty_Time":"M,M,M,M Sun-Fri",
  }
    ]
    return pd.DataFrame(data)

# ✅ Load Data
data = load_data()

# ✅ Display KE Logo
ke_logo_path = "https://vtlogo.com/wp-content/uploads/2020/03/k-electric-vector-logo.png"
st.image(ke_logo_path, width=120)



# ✅ Display Titles

st.markdown("<h4 style='text-align: center; color:#3498db;'>📋 DUTY ROASTER CM GIZRI \n\n (02ND MARCH TO 29TH MARCH)</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>🤵‍♂️ DGM CM Mr REHAN MURTAZA</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>👨‍💼 MANAGER CM Mr SAJID MEHMOOD</h5>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Dropdown for Selecting Team Member Type
view_option = st.selectbox("🔍 Find a Team Member Type:", ["Supervisor", "Linemen", "Fitter", "Karkun", "Employee Number"])

# ✅ Dropdown for Selecting Name
selected_name = None

if view_option == "Supervisor":
    selected_name = st.selectbox("Select a Supervisor:", [""] + data["Supervisor"].tolist())
elif view_option == "Linemen":
    selected_name = st.selectbox("Select a Lineman:", [""] + data["Lineman"].tolist())
elif view_option == "Fitter":
    selected_name = st.selectbox("Select a Fitter:", [""] + data["Fitter"].tolist())
elif view_option == "Karkun":
    selected_name = st.selectbox("Select a Karkun:", [""] + data["Karkun"].tolist())
elif view_option == "Employee Number":
    selected_name = st.selectbox("Select or type an Employee Number:", [""] + 
                                 pd.concat([data["Emp#"], data["Lineman_Emp#"], data["Fitter_Emp#"], data["Karkun_Emp#"]])
                                 .dropna().unique().tolist())

# ✅ Show Details Only After Selection
if selected_name and selected_name.strip():
    details = data[(data["Supervisor"] == selected_name) | 
                   (data["Lineman"] == selected_name) |
                   (data["Fitter"] == selected_name) | 
                   (data["Karkun"] == selected_name) |
                   (data["Emp#"] == selected_name) |
                   (data["Lineman_Emp#"] == selected_name) |
                   (data["Fitter_Emp#"] == selected_name) |
                   (data["Karkun_Emp#"] == selected_name)]
    
    if not details.empty:
        details = details.iloc[0]  # Get first matching record

        # ✅ Display Details in Card Format
        st.markdown("<div style='background-color: white; padding: 12px; border-radius: 8px; "
                    "box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);'>", unsafe_allow_html=True)
        st.markdown(f"<h5>🏷️ Supervisor: {details['Supervisor']} (Emp#: {details['Emp#']})</h5>", unsafe_allow_html=True)
        st.write(f"**🛠 Task:** {details['Task']}")
        st.write(f"**👷 Lineman:** {details['Lineman']} (Emp#: {details['Lineman_Emp#']})")
        st.write(f"**🔧 Fitter:** {details['Fitter']} (Emp#: {details['Fitter_Emp#']})")
        st.write(f"**📌 Karkun:** {details['Karkun']} (Emp#: {details['Karkun_Emp#']})")
        st.write(f"**📅 Off Day:** {details['Off_Day']}")
        st.write(f"**⏰ Duty Time:** {details['Duty_Time']}")
        st.markdown("</div>", unsafe_allow_html=True)
        

# ✅ Footer
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #555;'>🚀 This application is created by <b>Muhammad Yameen Saleem</b></p>", unsafe_allow_html=True)
