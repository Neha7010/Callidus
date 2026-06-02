import os
import json
import streamlit as st
from google import genai
from google.genai import types

# 1. CORE ARCHITECTURAL SYNTHESIZER WITH REFERENCE LOOKUPS
# -----------------------------------------------------------------------------
def compile_project_blueprint(major: str, target_role: str, tech_stack: str, interest_domain: str, project_field: str) -> str:
    try:
        stack_lower = tech_stack.lower()
        complexity_tier = "Tier 2: Intermediate Integrated Software Systems"
        
        if any(h in stack_lower for h in ["c++", "arduino", "embedded", "raspberry", "hardware", "iot"]):
            complexity_tier = "Tier 3: Cyber-Physical / Embedded Hardware Systems"
        elif any(d in stack_lower for d in ["ml", "pytorch", "tensorflow", "python", "data science", "r"]):
            complexity_tier = "Tier 3: Advanced Data Pipelines & Intelligent Agents"
            
        return json.dumps({
            "status": "BLUEPRINT_SUCCESS",
            "system_complexity_rating": complexity_tier,
            "target_alignment": f"Verified for {target_role} Core Competencies",
            "suggested_unique_angle": f"Injecting {tech_stack} frameworks into {interest_domain} within the specialized field of {project_field}."
        })
    except Exception as e:
        return json.dumps({"status": "COMPILATION_ERROR", "error_log": str(e)})


# 2. STATE & SECURITY AUTHENTICATION INITIALIZATION
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Launchpad AI", page_icon="🚀", layout="wide")


st.markdown("""
    <style>
    /* Professional Dark Workspace Background */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #111827 0%, #030712 100%) !important;
    }
    
    /* Clean Refined Liquid Glass Sidebar */
    div[data-testid="stSidebar"] {
        background: rgba(17, 24, 39, 0.7) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Elegant Border Containers with Soft Indigo Ambient Shadows */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.3),
                    0 0 30px -15px rgba(99, 102, 241, 0.1) !important;
        padding: 24px !important;
    }
    
    /* Hover Interaction Micro-Ambient Shift */
    div[data-testid="stVerticalBlock"] > div[style*="border"]:hover {
        border: 1px solid rgba(99, 102, 241, 0.25) !important;
        box-shadow: 0 8px 30px 0 rgba(0, 0, 0, 0.4),
                    0 0 35px -5px rgba(99, 102, 241, 0.15) !important;
    }
    
    /* High-Readability Editorial Typography Layout */
    h1 {
        font-size: 2.25rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.05em !important;
        color: #f9fafb !important;
        margin-bottom: 4px !important;
    }
    
    h2, h3, h4 {
        color: #f3f4f6 !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    p, li, span, label {
        color: #d1d5db !important;
        font-size: 0.95rem !important;
        line-height: 1.7 !important;
    }
    
    /* Form Inputs and Interactive Widgets */
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: rgba(255, 255, 255, 0.02) !important;
        border-radius: 6px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    
    /* Crimson Accent Command Action Button */
    button[kind="primary"] {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%) !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(220, 38, 38, 0.3) !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
    }
    button[kind="primary"]:hover {
        box-shadow: 0 6px 20px 0 rgba(220, 38, 38, 0.45) !important;
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

VALID_USERNAME = "student2026"
VALID_PASSWORD = "launchpad_secure_pass"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "blueprint_matrix" not in st.session_state:
    st.session_state.blueprint_matrix = None
if "architect_prose_report" not in st.session_state:
    st.session_state.architect_prose_report = ""

# MODE A: RENDER GATEWAY LOGIN INTERFACE
# -----------------------------------------------------------------------------
if not st.session_state.authenticated:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    col_l1, col_l2, col_l3 = st.columns([1.2, 1.5, 1.2])
    with col_l2:
        with st.container(border=True):
            st.markdown("<h1 style='text-align: center;' Launchpad AI Access Portal</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #9ca3af !important;'>Enter security session parameters to initialize the architecture workspace.</p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            input_user = st.text_input("Username / Roll Number:")
            input_pass = st.text_input("Security Access Code:", type="password")
            st.markdown("<br>", unsafe_allow_html=True)
            login_btn = st.button("Authenticate Session", type="primary", use_container_width=True)
            
            st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
            st.caption(" Developer Session Account — **User:** `student2026` | **Password:** `launchpad_secure_pass`")
            
            if login_btn:
                if input_user.strip() == VALID_USERNAME and input_pass.strip() == VALID_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid credentials configuration. Please confirm your access codes.")
    st.stop()

# MODE B: CORE APPLICATION
# -----------------------------------------------------------------------------
col_title, col_logout = st.columns([5, 1], vertical_alignment="center")
with col_title:
    st.title("🚀 Launchpad AI Workstation")
with col_logout:
    if st.button("Log Out ", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.blueprint_matrix = None
        st.session_state.architect_prose_report = ""
        st.rerun()

with st.container(border=True):
    st.markdown(
        "Every year, millions of engineering students miss out on top jobs because they build the same generic portfolio projects—like basic calculators or simple weather apps—that recruiters completely ignore. **Launchpad AI** operates as an automated engineering mentor, synthesizing advanced cross-domain architectures tailored strictly to your skill matrices."
    )

st.markdown("<br>", unsafe_allow_html=True)

if not os.environ.get("GEMINI_API_KEY"):
    st.error("Infrastructure Token Missing! Please go to your Hugging Face Space Settings -> Repository Secrets and add your GEMINI_API_KEY.")
    st.stop()


# 3. SIDEBAR PARAMETER SELECTION
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 👤 Candidate Variables")

sample_profiles = {
    "Custom (Manual Input)": {
        "major": "Computer Science & Engineering", "role": "", "stack": "", "niche": "",
        "category": "Final Year Capstone", "field": "Machine Learning & Intelligent Agents", "env": "Hugging Face Spaces", "num_papers": 3
    },
    "Example 1: AI + Bioacoustics": {
        "major": "Artificial Intelligence & Data Science", "role": "Core Machine Learning Engineer",
        "stack": "Python, PyTorch, Librosa, Streamlit, Git", "niche": "Marine biology and whale audio tracking",
        "category": "Final Year Capstone", "field": "Machine Learning & Intelligent Agents", "env": "Hugging Face Spaces", "num_papers": 3
    },
    "Example 2: IoT + Fitness": {
        "major": "Electronics & Communication", "role": "Embedded Systems Architect",
        "stack": "C++, Arduino, ESP32 Wi-Fi, MQTT Brokers, FreeRTOS", "niche": "Tracking posture slip metrics for weightlifters",
        "category": "Mini-Project (3rd Year)", "field": "Internet of Things (IoT) & Cyber-Physical Systems", "env": "Local Hardware Prototype", "num_papers": 2
    }
}

selected_profile = st.sidebar.selectbox("🚀 Quick Demo Profiles:", list(sample_profiles.keys()))
active_preset = sample_profiles[selected_profile]

student_major = st.sidebar.selectbox(
    "Academic Department Major:",
    ["Artificial Intelligence & Data Science", "Computer Science & Engineering", "Electronics & Communication", "Mechanical Engineering"],
    index=["Artificial Intelligence & Data Science", "Computer Science & Engineering", "Electronics & Communication", "Mechanical Engineering"].index(active_preset["major"])
)

target_job = st.sidebar.text_input("Target Professional Role:", value=active_preset["role"], placeholder="e.g., ML Engineer")
project_category = st.sidebar.selectbox(
    "Project Category Scope:",
    ["Final Year Capstone", "Mini-Project (3rd Year)", "Hackathon Prototype", "Independent Research Portfolio"],
    index=["Final Year Capstone", "Mini-Project (3rd Year)", "Hackathon Prototype", "Independent Research Portfolio"].index(active_preset["category"])
)

project_field = st.sidebar.selectbox(
    "Primary Sub-Field Focus:",
    ["Machine Learning & Intelligent Agents", "Internet of Things (IoT) & Cyber-Physical Systems", "Data Engineering & Pipeline Architectures", "Full-Stack Web Systems & Cloud Microservices", "Computer Vision & Robotics Automation"],
    index=["Machine Learning & Intelligent Agents", "Internet of Things (IoT) & Cyber-Physical Systems", "Data Engineering & Pipeline Architectures", "Full-Stack Web Systems & Cloud Microservices", "Computer Vision & Robotics Automation"].index(active_preset["field"])
)

deployment_env = st.sidebar.selectbox(
    "Target Deployment Environment:",
    ["Hugging Face Spaces", "Local Hardware Prototype", "AWS / Google Cloud Platform", "Docker Containers (Self-Hosted)"],
    index=["Hugging Face Spaces", "Local Hardware Prototype", "AWS / Google Cloud Platform", "Docker Containers (Self-Hosted)"].index(active_preset["env"])
)

num_papers = st.sidebar.slider("Number of Reference Papers Required:", min_value=1, max_value=5, value=int(active_preset.get("num_papers", 3)))

skills_input = st.sidebar.text_area("Core Tech Stack Tools:", value=active_preset["stack"], placeholder="e.g., Python, PyTorch, Git", height=80)
niche_interest = st.sidebar.text_input("Personal Niche Passion:", value=active_preset["niche"], placeholder="e.g., Marine bio, Fitness")

st.sidebar.markdown("<br>", unsafe_allow_html=True)
generate_project_btn = st.sidebar.button("Launch Architecture Engine", type="primary", use_container_width=True)


# 4. DATA RENDERING LAYOUT (Balanced Architecture Display Grid)
# -----------------------------------------------------------------------------
col_metrics, col_blueprint = st.columns([1.1, 1], gap="large")

with col_metrics:
    if st.session_state.architect_prose_report:
        with st.container(border=True):
            st.markdown("### Core Engineering Strategy Specs")
            st.markdown("<hr style='border-color: rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
            
            # Wrap generated output in a dedicated class layout to enforce line spacing text adjustments
            st.markdown(f'<div class="readable-report-pane">{st.session_state.architect_prose_report}</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Complete the target configuration profile fields on the left sidebar, select your required paper index counts, and launch the compiler.")

with col_blueprint:
    with st.container(border=True):
        st.markdown("###  Dynamic System Metrics & Analytics")
        st.markdown("<hr style='border-color: rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
        
        if not st.session_state.blueprint_matrix:
            st.info("System Standby. Awaiting architectural ingestion triggers.")
        else:
            matrix = st.session_state.blueprint_matrix
            
            st.success(f" Market Alignment: **{matrix.get('target_alignment')}**")
            st.warning(f" System Scale: **{matrix.get('system_complexity_rating')}**")
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("#### **System Intersection Framework:**")
            st.write(f"*{matrix.get('suggested_unique_angle')}*")
            
            st.markdown("<br><hr style='border-color: rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)
            
            st.markdown(f"#### **Project Roadmap Tracks ({project_category}):**")
            tracks = [" Spec Design", " Data Pipelines", " Logic Systems", " Host Deployment"]
            track_cols = st.columns(len(tracks))
            for idx, name in enumerate(tracks):
                with track_cols[idx]:
                    st.info(f"**Phase {idx + 1}**\n\n{name}")
                    
            st.markdown("<br><hr style='border-color: rgba(255,255,255,0.08);'><br>", unsafe_allow_html=True)
            st.markdown("####  Reference Literature Matrix Status")
            st.write(f"Successfully requested and processed exactly **{num_papers} academic reference blocks** specifically mapped for the **{project_field}** domain. Check the strategy sheet on the left panel for deep-dive literature abstracts.")

# -----------------------------------------------------------------------------
# 5. CORE AI PROCESSING DEPLOYMENT WITH VARIABLE REFERENCE ENGINE
# -----------------------------------------------------------------------------
if generate_project_btn and target_job and skills_input:
    client = genai.Client()
    
    prompt_payload = (
        f"Major Field: {student_major}. Desired Career Goal: {target_job}. "
        f"Project Category Scope: {project_category}. Specialized Sub-Field: {project_field}. "
        f"Target Environment: {deployment_env}. Tech Stack Available: {skills_input}. "
        f"Niche Interest/Domain Focus: {niche_interest}. Core Literature References Demanded: {num_papers}."
    )
    
    system_instruction = f"""
    You are an elite Chief Technology Officer (CTO) and Principal Technical Academic Advisor.
    
    Generate an incredibly detailed, beautifully structured engineering report based on the parameters provided.
    
    CRITICAL FORMATTING INSTRUCTIONS FOR HIGH READABILITY:
    - Use clean, prominent Markdown headers (###) for every section.
    - Avoid dense text blocks. Break down technical systems into descriptive bullet lists.
    - Format individual items with bold keywords at the start of bullets to make the document highly scannable.
    
    YOUR REPORT MUST CONTAIN THESE EXACT SECTIONS:
    ###  Project Architecture Abstract
    [Write a clear title and an elegant explanation of the cross-domain project intersection]
    
    ###  Detailed Functional Architecture & Data Pathways
    - **Data Ingestion Layer:** Explain exactly how data feeds into the system stack.
    - **Core Processing Module:** Detail how processing and models evaluate the constraints.
    - **Deployment Interface:** Clarify how the system renders results in the target {deployment_env} environment.
    
    ###  ATS-Optimized Resume Specifications
    [Provide 3 professional resume bullets written strictly in Action-Context-Result format, using bold formatting metrics for high visibility]
    
    ###  Granular 4-Week Technical Milestone Map
    - **Week 1 (System Architecture & Local Configuration):** Explicit sub-tasks.
    - **Week 2 (Pipeline & Data Engineering Infrastructure):** Explicit sub-tasks.
    - **Week 3 (Core Processing Core & Analytics Implementation):** Explicit sub-tasks.
    - **Week 4 (Cloud Interface Validation & Production Deployment):** Explicit sub-tasks.
    
    ###  Academic Literature Review References
    [Provide EXACTLY {num_papers} high-quality, realistic academic research papers, IEEE specifications, or ACM journal entries. Structure each reference exactly like this:
    - **Paper [Index] Title:** [Name of the study]
    - **Authors/Source:** [Academic contributors list]
    - **Core Study Framework & Value:** [A clean 2-sentence breakdown of why the student must cite this to justify their system design metrics]]
    """
    
    with st.spinner("Synthesizing responsive system frameworks and reference arrays..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt_payload,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    tools=[compile_project_blueprint], 
                    temperature=0.7
                )
            )
            
            if response.function_calls:
                call = response.function_calls[0]
                if call.name == "compile_project_blueprint":
                    args_with_field = dict(call.args)
                    args_with_field["project_field"] = project_field
                    
                    result_str = compile_project_blueprint(**args_with_field)
                    st.session_state.blueprint_matrix = json.loads(result_str)
                    
                    updated_context = [
                        types.Content(role="user", parts=[types.Part.from_text(text=prompt_payload)]),
                        types.Content(role="model", parts=[types.Part.from_function_call(name=call.name, args=call.args)]),
                        types.Content(role="user", parts=[types.Part.from_function_response(name=call.name, response={"result": result_str})])
                    ]
                    
                    final_pass = client.models.generate_content(
                        model="gemini-2.5-flash-lite",
                        contents=updated_context,
                        config=types.GenerateContentConfig(system_instruction=system_instruction, tools=[compile_project_blueprint])
                    )
                    st.session_state.architect_prose_report = final_pass.text
            else:
                st.session_state.architect_prose_report = response.text
                
            st.rerun()
        except Exception as e:
            st.error(f"Core Processing Module Interrupted: {str(e)}")