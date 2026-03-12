# theme.py
import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

    

def set_theme():
   
    st.markdown("""
    <style>
    /* Your entire CSS here, exactly as you have */
    .stApp {
        background: linear-gradient(to bottom, #01474d 0%);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: white;
        
    }




    /* Hide all Streamlit top-right menu items */
    #MainMenu, header [data-testid="collapsedControl"] {
        display: none !important;
        }

    /* sidebar arrow */
    [data-testid="stExpandSidebarButton"] {
    margin-top: 150px !important;
    }



    h1{
        
       padding-top:0px; !important;
       font-family: 'Arial', serif;
        font-size: 48px;
        font-weight: 700;
        text-align: left;      /* align text left */
        margin-left: 90%;      
        }
    
    p{
     color:white; 
      }
    
    
    
    hr{
       margin-top:-5px !important;
       }
    
    div[data-testid="stHeading"] h1 {
    font-size: 19px !important;
}    
    
    .st-emotion-cache-p38tq {
        color: white; 
        }

 
    
    /* Fix header/title area */
    header, .block-container {
        background-color: transparent !important;
         padding-top: 0px !important;
        margin-top: -40px !important;
        
    }
    
   section[data-testid="stSidebar"][aria-expanded="true"] {
    width: 250px !important;
    min-width: 250px !important;
    max-width: 250px !important;
    }

    
    /* Sidebar */
   section[data-testid="stSidebar"] {
       background: linear-gradient(to bottom, #01474d);
       border-right: 2px solid #2c3e50;
       
       
   }
                                   
   [data-testid="stSidebarHeader"]{
       margin-top:30px;
       }

   /* Sidebar title */
   .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4 {
       color: #ffffff;
   }

   /* Sidebar radio buttons */
   div[role="radiogroup"] > label {
       background-color: rgba(255, 255, 255, 0.1);
       backdrop-filter: blur(8px);
       box-shadow: 0 4px 20px rgba(0,0,0,0.25);
       color: white;
       padding: 0.5rem 1rem;
       border-radius: 30px;
       margin: 0.2rem 0;
       min-width:200px;
       transition: all 0.3s ease;
       border: 1px solid transparent;
   }

   
   

   /* Hover effect */
   div[role="radiogroup"] > label:hover {
       box-shadow: 0 0 10px rgba(93, 173, 226, 0.6);
   }

   /* Selected item */
   div[role="radiogroup"] > label[data-selected="true"] {
       background-color: #5dade2;
       color: black;
       font-weight: bold;
       border: 1px solid #ffffff;
   }
   
   .stCheckbox
   {
    margin-left:50px;
    
    }
   

    


 
   .stPlotlyChart{
       border-radius: 20px !important;   /* Rounded corners */
       overflow: hidden;                 /* Clip contents */
       box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Optional shadow */
       border: 2px solid white;
       }
   
   
   
   /* New Floating Circles */
    .floating-circles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 1;
    }

   .floating-circles div {
    position: absolute;
    border-radius: 16px;   /* 👈 rounded square */
    background: rgba(255, 255, 255, 0.1);
    animation: float 15s linear infinite;
    opacity: 0.3;
}










    .circle1 { width: 120px; height: 120px; top: 10%; left: 20%; animation-duration: 18s; }
    .circle2 { width: 80px; height: 80px; top: 30%; left: 95%; animation-duration: 20s; }
    .circle3 { width: 150px; height: 150px; top: 70%; left: 10%; animation-duration: 22s; }
    .circle4 { width: 60px; height: 60px; top: 65%; left: 92%; animation-duration: 16s; }
    .circle5 { width: 60px; height: 40px; top: 85%; left: 95%; animation-duration: 16s; }
    .circle6 { width: 120px; height: 60px; top: 55%; left: 10%; animation-duration: 16s; }
    .circle7 { width: 60px; height: 60px; top: 25%; left: 95%; animation-duration: 16s; }

    @keyframes float {
        0%   {transform: translateY(0) translateX(0); opacity: 0.3;}
        50%  {transform: translateY(-40px) translateX(20px); opacity: 0.5;}
        100% {transform: translateY(0) translateX(0); opacity: 0.3;}
    }
    
    /* Image next to sidebar, dynamic position */
    .top-left-image {
        position: absolute;
        top: 20px;
        left: calc(1rem + 0px); /* fallback value */
        margin-left: -70px; /* Sidebar default width */
        width: 80px;
        height: auto;
        z-index: 10;
        transition: margin-left 0.3s ease;
    }

    /* When sidebar is collapsed (Streamlit sets this class on narrow screens) */
    @media screen and (max-width: 768px) {
        .top-left-image {
            margin-left: 0;
        }
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    img_base64 = get_base64_image("images/nama1.png")
    st.markdown(f"""
    <img class="top-left-image" src="data:image/png;base64,{img_base64}" alt="Top Left Logo" style="height: 110px; width:150px; margin-top:12px; margin-left:-35px" />
    """, unsafe_allow_html=True)
    
    galfar_img = get_base64_image("images/logo.png")

    
    st.markdown(
    f"""
    <div style="position: absolute; top: 30px; right:-80px; display: flex; gap: 8px; z-index: 1000;">
        <img src="data:image/png;base64,{galfar_img}" alt="Galfar" style="height: 70px; width:auto; margin-top:0px; margin-right:-20px;" />

    </div>
    """,
    unsafe_allow_html=True
)


    st.markdown("""
    <div class="floating-circles">
        <div class="circle1"></div>
        <div class="circle2"></div>
        <div class="circle3"></div>
        <div class="circle4"></div>
        <div class="circle5"></div>
        <div class="circle6"></div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown(
    """
    <style>
    /* Glass selectbox container */
    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.18) !important;
        backdrop-filter: blur(14px) saturate(160%);
        -webkit-backdrop-filter: blur(14px) saturate(160%);
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        color: white;
    }

    /* Selected text */
    div[data-baseweb="select"] span {
        color: white !important;
        font-weight: 500;
    }

    /* Dropdown arrow */
    div[data-baseweb="select"] svg {
        fill: white !important;
    }

    /* Dropdown menu */
    ul {
        background: #01474d !important;
        backdrop-filter: blur(12px);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.2);
    }

    ul li {
        color: white !important;
        
    }

    /* Hover option */
    li:hover {
        background: rgba(255,255,255,0.15) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
























































