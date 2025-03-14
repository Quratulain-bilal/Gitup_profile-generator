import streamlit as st

# Inline CSS for full-page glassmorphism effect
st.markdown(
    """
<style>
/* Main Page Background with Glassmorphism */
.stApp {
    background: url('https://e0.pxfuel.com/wallpapers/618/263/desktop-wallpaper-github-logo-cut-out-3d-text-white-background-github-3d-logo-github-emblem-github-embossed-logo-github-3d-emblem.jpg') no-repeat center center fixed;
    background-size: cover;
    min-height: 100vh; /* Full page height */
    padding-top: 0 !important; /* Remove white space at the top */
    backdrop-filter: blur(3px); /* Blur the background image */
}

/* Background Overlay with Opacity */
.stApp::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.4); /* Light overlay for better contrast */
    backdrop-filter: blur(3px); /* Additional blur effect */
    z-index: -1; /* Place behind content */
}

/* Main Content Container */
.main-content {
    position: relative;
    z-index: 1; /* Place above the glassmorphism overlay */
    background: rgba(255, 255, 255, 0.9); /* Slightly opaque white */
    border-radius: 15px; /* Rounded corners */
    padding: 20px; /* Padding for content */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); /* Shadow for depth */
    margin: 20px auto; /* Center the container */
    width: 90%; /* Width of the container */
    max-width: 1200px; /* Maximum width */
}

/* Text Styling */
h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stTextInput label, .stButton button, .stFileUploader label {
    font-family: 'Poppins', sans-serif; /* Modern font family */
    font-weight: bold !important;
    color: #333333 !important; /* Dark gray text for better visibility */
}

/* Increase Font Sizes */
h1 {
    font-size: 2.5rem; /* Larger heading */
    margin-bottom: 15px;
}
h2 {
    font-size: 2rem;
    margin-bottom: 10px;
}
h3 {
    font-size: 1.75rem;
    margin-bottom: 10px;
}
p, label, .stMarkdown, .stTextInput label, .stButton button, .stFileUploader label {
    font-size: 1.2rem; /* Larger text for readability */
}

/* Input Fields Styling */
.stTextInput input, .stMultiselect div, .stCheckbox div {
    background: rgba(255, 255, 255, 0.8);
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    font-size: 1.1rem; /* Larger input text */
    font-family: 'Poppins', sans-serif; /* Consistent font */
    color: #333333 !important; /* Dark gray text for inputs */
}
.stTextInput input:focus, .stMultiselect div:focus, .stCheckbox div:focus {
    transform: scale(1.02);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

/* Glowing Buttons */
.stButton button {
    background: linear-gradient(135deg, #ff6f61, #ffcc00) !important;
    color: #ffffff !important; /* White text for buttons */
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 25px !important;
    font-size: 1.2rem !important; /* Larger button text */
    font-family: 'Poppins', sans-serif; /* Consistent font */
    cursor: pointer !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    box-shadow: 0 0 10px rgba(255, 111, 97, 0.7) !important;
}
.stButton button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 20px rgba(255, 111, 97, 1) !important;
}

/* Tech Stack Icons */
.tech-icons {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    justify-content: center;
}
.tech-icons img {
    width: 100px;
    height: auto;
    transition: transform 0.3s ease;
}
.tech-icons img:hover {
    transform: scale(1.1);
}
</style>
    """,
    unsafe_allow_html=True,
)

# Two-Column Layout
st.markdown('<div class="main-content">', unsafe_allow_html=True)  # Open main content container

# Left Column for Inputs
# Title and Image Below Heading
st.markdown("""
<h1 style="text-align: center;"> Generate a Stunning GitHub Profile in Seconds</h1>
<div style="text-align: center;">
    <img src="https://letmefail.com/wp-content/uploads/2022/09/github-readme-profile-1.png" alt="GitHub Profile Image" style="width: 80%; max-width: 600px; margin: 20px auto; border-radius: 10px;">
</div>
""", unsafe_allow_html=True)
# User Inputs
name = st.text_input("Your Name", "Quratulain Shah")
profession = st.text_input("Your Profession", "Frontend Developer")
location = st.text_input("Your Location", "Pakistan")

# Tech Stack
st.subheader("Tech Stack")
tech_options = [
    "Next.js", "React", "Tailwind CSS", "JavaScript", "TypeScript",
    "HTML", "CSS", "Python", "Streamlit", "Node.js", "Git",
    "Docker", "Kubernetes", "GraphQL", "MongoDB", "PostgreSQL",
    "Firebase", "AWS", "Azure", "GCP", "Flutter", "Swift"
]
selected_tech = st.multiselect("Select Your Tech Stack", tech_options, default=["Next.js", "React", "Tailwind CSS"])

# Social Media Links
st.subheader("Social Media Links")
github = st.text_input("GitHub Profile URL", "https://github.com/Quratulain-bilal")
linkedin = st.text_input("LinkedIn Profile URL", "https://www.linkedin.com/in/quratulain-shah-7bb869316")
twitter = st.text_input("Twitter Profile URL", "https://twitter.com/stelalvna")
gmail = st.text_input("Gmail Address", "aimoshahs@gmail.com")
instagram = st.text_input("Instagram Profile URL", "https://instagram.com/")
youtube = st.text_input("YouTube Channel URL", "https://youtube.com/")
portfolio = st.text_input("Portfolio Website URL", "https://yourportfolio.com/")

# GitHub Stats
st.subheader("GitHub Stats")
show_stats = st.checkbox("Show GitHub Stats", True)
show_streak = st.checkbox("Show GitHub Streak", True)
show_languages = st.checkbox("Show Top Languages", True)

# Snake Animation
show_snake = st.checkbox("Show Snake Animation", True)

# Template Selection
st.subheader("Choose a Template")
template = st.radio("Select Template", ["Simple", "Professional"])

# Generate README
if st.button("Generate README 🎉"):
    # Tech Stack Icons
    tech_icons = {
        "Next.js": "https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white",
        "React": "https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB",
        "Tailwind CSS": "https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white",
        "JavaScript": "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black",
        "TypeScript": "https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white",
        "HTML": "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
        "CSS": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
        "Python": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
        "Streamlit": "https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white",
        "Node.js": "https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white",
        "Git": "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
        "Docker": "https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white",
        "Kubernetes": "https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white",
        "GraphQL": "https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white",
        "MongoDB": "https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white",
        "PostgreSQL": "https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white",
        "Firebase": "https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=white",
        "AWS": "https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white",
        "Azure": "https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white",
        "GCP": "https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white",
        "Flutter": "https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white",
        "Swift": "https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white"
    }

    # README Content Based on Template
    if template == "Simple":
        readme = f"""
# Hi 👋, I'm {name}
## {profession} from {location}
---
### 🛠️ Tech Stack
<div class="tech-icons">
"""
        for tech in selected_tech:
            readme += f'  <img src="{tech_icons[tech]}" alt="{tech}" />\n'
        readme += "</div>\n---\n"

        if show_stats or show_streak or show_languages:
            readme += "### 📊 GitHub Stats\n<div align=\"center\">\n"
            if show_stats:
                readme += f'  <img src="https://github-readme-stats.vercel.app/api?username={github.split("/")[-1]}&show_icons=true&theme=default&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" width="48%" />\n'
            if show_streak:
                readme += f'  <img src="https://github-readme-streak-stats.herokuapp.com/?user={github.split("/")[-1]}&theme=default&hide_border=true" alt="GitHub Streak" width="48%" />\n'
            if show_languages:
                readme += f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={github.split("/")[-1]}&layout=compact&theme=default&hide_border=true" alt="Top Languages" width="48%" />\n'
            readme += "</div>\n---\n"

        if show_snake:
            readme += """
### 🐍 Snake Eating My Contributions
<div align="center">
  <img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="Snake Animation" />
</div>
---
"""
        readme += """
### 💬 Let's Connect!
<p align="center">
  <a href="{linkedin}" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="{twitter}" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter" />
  </a>
  <a href="mailto:{gmail}" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  <a href="{instagram}" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="{youtube}" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  </a>
  <a href="{portfolio}" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=portfolio&logoColor=white" alt="Portfolio" />
  </a>
</p>
"""

    elif template == "Professional":
        readme = f"""
<h1 align="center">Hi 👋, I'm {name}</h1>
<h3 align="center">{profession} from {location}</h3>
<p align="center">
  <a href="{github}">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=00FF00&center=true&vCenter=true&width=435&lines=Turning+Ideas+into+Reality;Building+Modern+Web+Apps;Always+Learning+%26+Growing" alt="Typing SVG" />
  </a>
</p>
---
### 🛠️ Tech Stack
<div class="tech-icons">
"""
        for tech in selected_tech:
            readme += f'  <img src="{tech_icons[tech]}" alt="{tech}" />\n'
        readme += "</div>\n---\n"

        if show_stats or show_streak or show_languages:
            readme += "### 📊 GitHub Stats\n<div align=\"center\">\n"
            if show_stats:
                readme += f'  <img src="https://github-readme-stats.vercel.app/api?username={github.split("/")[-1]}&show_icons=true&theme=dark&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" width="48%" />\n'
            if show_streak:
                readme += f'  <img src="https://github-readme-streak-stats.herokuapp.com/?user={github.split("/")[-1]}&theme=dark&hide_border=true" alt="GitHub Streak" width="48%" />\n'
            if show_languages:
                readme += f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={github.split("/")[-1]}&layout=compact&theme=dark&hide_border=true" alt="Top Languages" width="48%" />\n'
            readme += "</div>\n---\n"

        if show_snake:
            readme += """
### 🐍 Snake Eating My Contributions
<div align="center">
  <img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="Snake Animation" />
</div>
---
"""
        readme += """
### 💬 Let's Connect!
<p align="center">
  <a href="{linkedin}" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="{twitter}" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter" />
  </a>
  <a href="mailto:{gmail}" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  <a href="{instagram}" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="{youtube}" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  </a>
  <a href="{portfolio}" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=portfolio&logoColor=white" alt="Portfolio" />
  </a>
</p>
"""

    # Display Generated Code
    st.subheader("Generated README Code")
    st.code(readme, language="markdown")

    # Download Button
    st.download_button(
        label="Download README 📄",
        data=readme,
        file_name="README.md",
        mime="text/markdown"
    )

st.markdown('</div>', unsafe_allow_html=True)  # Close left column

# Right Column for Preview
st.markdown('<div class="right-column">', unsafe_allow_html=True)
st.subheader("Preview Your README")
if "readme" in locals():
    st.markdown(readme, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close right column

st.markdown('</div>', unsafe_allow_html=True)  # Close main content container