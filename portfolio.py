import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Aleena Anam | AI/ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: #0a0a0f;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .bg-glow {
        position: fixed;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(ellipse at 30% 20%, rgba(108, 99, 255, 0.12) 0%, transparent 50%),
                    radial-gradient(ellipse at 70% 80%, rgba(255, 99, 132, 0.08) 0%, transparent 50%),
                    #0a0a0f;
        z-index: -1;
        animation: gradientShift 15s ease infinite;
    }
    
    .hero {
        padding: 4rem 0 2rem 0;
        text-align: center;
        position: relative;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(108, 99, 255, 0.15);
        color: #6C63FF;
        padding: 0.4rem 1.5rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 1px;
        border: 1px solid rgba(108, 99, 255, 0.2);
        backdrop-filter: blur(10px);
        margin-bottom: 1.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .hero h1 {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6C63FF 0%, #a78bfa 30%, #f472b6 60%, #fb923c 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 6s ease infinite;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    
    .hero .subtitle {
        font-size: 1.4rem;
        color: #a0a0b0;
        font-weight: 400;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }
    
    .hero .tagline {
        font-size: 1.1rem;
        color: #808090;
        max-width: 650px;
        margin: 1rem auto 2rem;
        line-height: 1.8;
    }
    
    .btn-group {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin: 1.5rem 0;
    }
    
    .btn-primary {
        display: inline-block;
        padding: 0.9rem 2.8rem;
        background: linear-gradient(135deg, #6C63FF, #8B5CF6);
        color: white !important;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 20px rgba(108, 99, 255, 0.3);
        border: none;
        cursor: pointer;
    }
    
    .btn-primary:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 40px rgba(108, 99, 255, 0.5);
    }
    
    .btn-secondary {
        display: inline-block;
        padding: 0.9rem 2.8rem;
        background: rgba(255,255,255,0.05);
        color: #e0e0e0 !important;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        backdrop-filter: blur(10px);
    }
    
    .btn-secondary:hover {
        background: rgba(255,255,255,0.1);
        border-color: rgba(108, 99, 255, 0.4);
        transform: translateY(-3px) scale(1.05);
    }
    
    .stat-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: rgba(255,255,255,0.03);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
        text-align: center;
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.06);
        border-color: rgba(108, 99, 255, 0.2);
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .stat-number {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6C63FF, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-number.pink { background: linear-gradient(135deg, #f472b6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stat-number.orange { background: linear-gradient(135deg, #fb923c, #f97316); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stat-number.green { background: linear-gradient(135deg, #34d399, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    .stat-label {
        color: #808090;
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }
    
    .contact-bar {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.5rem 3rem;
        padding: 1.2rem 2rem;
        background: rgba(255,255,255,0.03);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
        backdrop-filter: blur(20px);
        margin: 1rem 0 2rem;
        transition: all 0.3s;
    }
    
    .contact-bar:hover {
        border-color: rgba(108, 99, 255, 0.15);
    }
    
    .contact-bar a, .contact-bar span {
        color: #a0a0b0;
        text-decoration: none;
        font-size: 0.95rem;
        transition: all 0.3s;
    }
    
    .contact-bar a:hover {
        color: #6C63FF;
        transform: translateY(-2px);
    }
    
    .section-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 3rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        background: linear-gradient(135deg, #fff 30%, #6C63FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #6C63FF, transparent);
        border-radius: 2px;
    }
    
    .exp-card {
        background: rgba(255,255,255,0.03);
        padding: 1.8rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.06);
        border-left: 4px solid #6C63FF;
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: default;
    }
    
    .exp-card:hover {
        background: rgba(255,255,255,0.06);
        transform: translateX(10px) scale(1.01);
        border-color: rgba(108, 99, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .exp-card h3 {
        font-weight: 700;
        color: #fff;
        font-size: 1.2rem;
        margin-bottom: 0.2rem;
    }
    
    .exp-card .company {
        font-weight: 600;
        color: #6C63FF;
        font-size: 0.95rem;
    }
    
    .exp-card .date {
        color: #666;
        font-size: 0.85rem;
        margin-bottom: 0.8rem;
    }
    
    .exp-card ul {
        padding-left: 1.2rem;
        margin-bottom: 0;
    }
    
    .exp-card li {
        font-size: 0.95rem;
        color: #b0b0c0;
        line-height: 1.7;
        margin-bottom: 0.3rem;
        list-style-type: '▸ ';
    }
    
    .exp-card li::marker {
        color: #6C63FF;
    }
    
    .project-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }
    
    @media (max-width: 768px) {
        .project-grid {
            grid-template-columns: 1fr;
        }
        .stat-grid {
            grid-template-columns: 1fr 1fr;
        }
    }
    
    .project-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        padding: 1.8rem;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        position: relative;
        overflow: hidden;
        cursor: default;
    }
    
    .project-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 30%, rgba(108, 99, 255, 0.05), transparent 60%);
        opacity: 0;
        transition: opacity 0.6s;
    }
    
    .project-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(108, 99, 255, 0.3);
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    .project-card:hover::before {
        opacity: 1;
    }
    
    .project-card h4 {
        font-weight: 700;
        color: #fff;
        font-size: 1.15rem;
        margin-bottom: 0.2rem;
    }
    
    .project-card .tech {
        font-size: 0.8rem;
        color: #6C63FF;
        font-weight: 600;
        margin-bottom: 0.8rem;
        letter-spacing: 0.5px;
    }
    
    .project-card p {
        font-size: 0.92rem;
        color: #a0a0b0;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .project-links a {
        color: #6C63FF;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        margin-right: 1.5rem;
        transition: all 0.3s;
        position: relative;
        z-index: 1;
        display: inline-block;
    }
    
    .project-links a:hover {
        color: #a78bfa;
        transform: translateX(3px);
    }
    
    .skill-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
    }
    
    .skill-category {
        background: rgba(255,255,255,0.03);
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
        transition: all 0.3s;
    }
    
    .skill-category:hover {
        background: rgba(255,255,255,0.06);
        border-color: rgba(108, 99, 255, 0.2);
        transform: translateY(-3px);
    }
    
    .skill-category h5 {
        font-weight: 600;
        color: #fff;
        font-size: 0.95rem;
        margin-bottom: 0.8rem;
        letter-spacing: 0.5px;
    }
    
    .skill-tag {
        display: inline-block;
        background: rgba(108, 99, 255, 0.1);
        color: #a78bfa;
        padding: 0.25rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.15rem;
        border: 1px solid rgba(108, 99, 255, 0.15);
        transition: all 0.3s;
        cursor: default;
    }
    
    .skill-tag:hover {
        background: rgba(108, 99, 255, 0.2);
        transform: scale(1.08) rotate(-2deg);
        border-color: rgba(108, 99, 255, 0.3);
    }
    
    .cert-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
    }
    
    .cert-badge {
        background: rgba(255,255,255,0.04);
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        border: 1px solid rgba(255,255,255,0.06);
        color: #b0b0c0;
        transition: all 0.3s;
        cursor: default;
    }
    
    .cert-badge:hover {
        background: rgba(108, 99, 255, 0.1);
        border-color: rgba(108, 99, 255, 0.2);
        color: #fff;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 5px 20px rgba(108, 99, 255, 0.1);
    }
    
    .edu-card {
        background: rgba(255,255,255,0.03);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
        backdrop-filter: blur(10px);
        transition: all 0.3s;
    }
    
    .edu-card:hover {
        border-color: rgba(108, 99, 255, 0.2);
        transform: translateX(5px);
    }
    
    .edu-card h3 {
        color: #fff;
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    .edu-card .uni {
        color: #a0a0b0;
    }
    
    .edu-card .gpa {
        color: #6C63FF;
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    .footer {
        text-align: center;
        color: #555;
        font-size: 0.85rem;
        padding: 3rem 0 2rem;
        border-top: 1px solid rgba(255,255,255,0.05);
        margin-top: 2rem;
    }
    
    .footer a {
        color: #6C63FF;
        text-decoration: none;
        transition: color 0.3s;
    }
    
    .footer a:hover {
        color: #a78bfa;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0a0a0f;
    }
    ::-webkit-scrollbar-thumb {
        background: #6C63FF;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #8B5CF6;
    }
    
    @media (max-width: 768px) {
        .hero h1 {
            font-size: 2.8rem;
        }
        .hero .subtitle {
            font-size: 1.1rem;
        }
        .section-title {
            font-size: 1.6rem;
        }
        .contact-bar {
            gap: 0.8rem 1.5rem;
            padding: 1rem;
        }
        .stat-grid {
            grid-template-columns: 1fr 1fr;
            gap: 0.8rem;
        }
        .stat-number {
            font-size: 2rem;
        }
    }
    
    @media (max-width: 480px) {
        .hero h1 {
            font-size: 2.2rem;
        }
        .btn-primary, .btn-secondary {
            padding: 0.7rem 1.8rem;
            font-size: 0.9rem;
        }
        .stat-grid {
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
        }
        .stat-card {
            padding: 1rem;
        }
        .stat-number {
            font-size: 1.6rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- ANIMATED BACKGROUND ---
st.markdown('<div class="bg-glow"></div>', unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Available for Remote Roles</div>
    <h1>Aleena Anam</h1>
    <p class="subtitle">AI/ML Engineer · Data Scientist · GenAI Developer</p>
    <p class="tagline">
        Building production-ready ML pipelines, GenAI applications, and data-driven dashboards.
        <br>3 internships · 7 live projects · 13+ certifications
    </p>
    <div class="btn-group">
        <a href="#projects" class="btn-primary">🚀 View My Work</a>
        <a href="#contact" class="btn-secondary">✉️ Contact Me</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- STATS ---
st.markdown("""
<div class="stat-grid">
    <div class="stat-card">
        <div class="stat-number">3+</div>
        <div class="stat-label">Internships</div>
    </div>
    <div class="stat-card">
        <div class="stat-number pink">7</div>
        <div class="stat-label">Live Projects</div>
    </div>
    <div class="stat-card">
        <div class="stat-number orange">13+</div>
        <div class="stat-label">Certifications</div>
    </div>
    <div class="stat-card">
        <div class="stat-number green">9.1</div>
        <div class="stat-label">GPA / 10</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CONTACT BAR ---
st.markdown("""
<div class="contact-bar" id="contact">
    <span>📧 <a href="mailto:anamaleena0@gmail.com">anamaleena0@gmail.com</a></span>
    <span>📱 +91 9175797672</span>
    <span>📍 Nanded, Maharashtra · Remote</span>
    <span>🔗 <a href="https://github.com/anam-aleena" target="_blank">GitHub</a></span>
    <span>📊 <a href="https://public.tableau.com/app/profile/aleena.anam" target="_blank">Tableau</a></span>
    <span>💼 <a href="https://www.linkedin.com/in/aleena-anam-2056a4368/" target="_blank">LinkedIn</a></span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- ABOUT ---
st.markdown('<div class="section-title">✦ About Me</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color: #c0c0d0; font-size: 1.05rem; line-height: 1.9; max-width: 900px;">
    I'm an AI/ML Engineer and Data Scientist with hands-on experience building, deploying, and 
    documenting end-to-end ML pipelines, GenAI applications, and data visualisation dashboards 
    across <strong style="color: #6C63FF;">3 industry internships</strong> and 
    <strong style="color: #6C63FF;">7 live projects</strong>.
    <br><br>
    Proficient in Python, Scikit-learn, TensorFlow, LangChain, FAISS, Tableau, SQL, and cloud 
    platforms including Microsoft Azure and Google Cloud. Built and deployed a live RAG PDF Chatbot 
    using LangChain + FAISS + Gemini 2.5 Flash. Published a Tableau dashboard revealing 
    <strong style="color: #f472b6;">99.5% complaint-churn correlation</strong> across 10,000 banking customers.
    <br><br>
    <span style="background: rgba(108,99,255,0.1); padding: 0.3rem 1.5rem; border-radius: 50px; border: 1px solid rgba(108,99,255,0.15); display: inline-block;">
        🎓 GPA: 9.1/10 · 13+ certifications in AI Agents, LLMs, and GenAI
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- EXPERIENCE ---
st.markdown('<div class="section-title">✦ Experience</div>', unsafe_allow_html=True)

exp_data = [
    {
        "title": "ML Data Scientist Intern",
        "company": "Microsoft Elevate × AICTE × Edunet Foundation",
        "date": "Jan 2026 — Feb 2026",
        "points": [
            "Built and deployed fraud detection ML pipeline comparing Logistic Regression, Random Forest, and XGBoost; deployed XGBoost as live REST API on Microsoft Azure",
            "Performed end-to-end data preprocessing: feature engineering, SMOTE class balancing, StandardScaler normalization",
            "Delivered production deployment from raw data to live API endpoint, minimizing false negatives through iterative threshold tuning"
        ]
    },
    {
        "title": "AI/ML Engineering Intern",
        "company": "AICTE × IBM SkillsBuild × Edunet Foundation",
        "date": "Jan 2026 — Feb 2026",
        "points": [
            "Applied ML algorithms to real-world AI scenarios using Python and Scikit-learn",
            "Researched LLM architectures, GenAI deployment patterns, and AI agent design through IBM SkillsBuild curriculum"
        ]
    },
    {
        "title": "Data Science Intern",
        "company": "Internship Studio (iStudio)",
        "date": "Jul 2025 — Oct 2025",
        "points": [
            "Collected, cleaned, and preprocessed large-scale structured datasets using Python, Pandas, and NumPy",
            "Conducted EDA identifying trends and patterns, produced visualizations with Matplotlib and Seaborn",
            "Developed and validated predictive ML models across classification, regression, and clustering tasks"
        ]
    }
]

for exp in exp_data:
    points_html = "".join([f"<li>{point}</li>" for point in exp["points"]])
    st.markdown(f"""
    <div class="exp-card">
        <h3>{exp['title']}</h3>
        <div class="company">{exp['company']}</div>
        <div class="date">{exp['date']}</div>
        <ul>{points_html}</ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- PROJECTS ---
st.markdown('<div class="section-title" id="projects">✦ Live Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "RAG PDF Chatbot",
        "tech": "LangChain · FAISS · Gemini 2.5 Flash · Streamlit",
        "desc": "Production RAG pipeline: PDF loading, chunking, HuggingFace embeddings, FAISS vector search, Gemini 2.5 Flash generation. Returns grounded answers with exact page citations.",
        "links": [("🔗 Live App", "https://rag-pdf-chatbot-a1.streamlit.app"), ("📁 GitHub", "https://github.com/anam-aleena/rag-pdf-chatbot")]
    },
    {
        "title": "Bank Customer Churn Dashboard",
        "tech": "Tableau · 10,000 customers",
        "desc": "6 interactive visualizations revealing key churn drivers: 99.5% complaint-churn correlation, Germany 32.4% churn rate, customers with 3-4 products churning at 83-100%.",
        "links": [("🔗 Live Dashboard", "https://public.tableau.com/app/profile/aleena.anam/viz/bankchurndashborad/Dashboard1")]
    },
    {
        "title": "Online Payment Fraud Detection",
        "tech": "XGBoost · SMOTE · Azure",
        "desc": "Fraud detection system on 6M+ financial records. Full pipeline from raw data to live REST API deployed on Microsoft Azure for real-time classification.",
        "links": [("📁 GitHub", "https://github.com/anam-aleena/online_paymentfrauddetection_aleenaanam")]
    },
    {
        "title": "AI Resume Screener",
        "tech": "TF-IDF · FastAPI · NLP",
        "desc": "TF-IDF + cosine similarity + 200+ skill taxonomy. 5-dimension weighted scoring engine. FastAPI REST API batch-processing 50+ resumes simultaneously.",
        "links": [("📁 GitHub", "https://github.com/anam-aleena/ai-resume-screener")]
    },
    {
        "title": "MNIST Digit Classifier",
        "tech": "TensorFlow · Keras · CNN",
        "desc": "CNN achieving ~99.4% test accuracy with BatchNorm, Dropout, data augmentation. Deployed as FastAPI REST API with streaming inference endpoint.",
        "links": [("📁 GitHub", "https://github.com/anam-aleena/tensorflow-mnist-classifier")]
    },
    {
        "title": "Customer Churn Prediction",
        "tech": "Scikit-learn · XGBoost",
        "desc": "End-to-end ML pipeline: EDA, feature engineering, model comparison (LR, RF, GBM, XGBoost). XGBoost achieved ~0.91 ROC-AUC.",
        "links": [("📁 GitHub", "https://github.com/anam-aleena/customer-churn-prediction")]
    }
]

st.markdown('<div class="project-grid">', unsafe_allow_html=True)
for project in projects:
    links_html = "".join([f'<a href="{link[1]}" target="_blank">{link[0]}</a>' for link in project["links"]])
    st.markdown(f"""
    <div class="project-card">
        <h4>{project['title']}</h4>
        <div class="tech">{project['tech']}</div>
        <p>{project['desc']}</p>
        <div class="project-links">{links_html}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- SKILLS ---
st.markdown('<div class="section-title">✦ Technical Skills</div>', unsafe_allow_html=True)

skills = {
    "🧠 ML & Modeling": ["Scikit-learn", "XGBoost", "Random Forest", "Logistic Regression", "Classification", "Regression", "Clustering", "Cross-Validation", "ROC-AUC", "SMOTE", "Feature Engineering"],
    "🤖 GenAI & LLMs": ["LangChain", "FAISS", "RAG Pipelines", "Google Gemini API", "HuggingFace", "AI Agents", "Prompt Engineering", "Vector Databases"],
    "📊 Data & Visualization": ["Python", "Pandas", "NumPy", "Tableau", "Matplotlib", "Seaborn", "Plotly", "SQL", "EDA"],
    "🧬 Deep Learning": ["TensorFlow", "Keras", "CNN", "Neural Networks", "PyTorch"],
    "☁️ Cloud & APIs": ["Microsoft Azure", "Google Cloud", "Oracle OCI", "FastAPI", "Streamlit", "REST APIs", "Git", "GitHub"]
}

st.markdown('<div class="skill-grid">', unsafe_allow_html=True)
for category, items in skills.items():
    tags = "".join([f'<span class="skill-tag">{skill}</span> ' for skill in items])
    st.markdown(f"""
    <div class="skill-category">
        <h5>{category}</h5>
        <div>{tags}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- CERTIFICATIONS ---
st.markdown('<div class="section-title">✦ Certifications</div>', unsafe_allow_html=True)

certs = [
    "AI Agents Intensive — Google/Kaggle",
    "Intro to LLMs — Google Cloud",
    "Oracle AI Vector Search",
    "OCI Data Science Professional — Oracle",
    "OCI AI Foundations — Oracle",
    "Microsoft Copilot Studio",
    "AI Concepts — Microsoft",
    "Microsoft Data Analytics",
    "Python 101 — IBM",
    "McKinsey Forward Program",
    "BCG X Data Analytics",
    "OCI Foundations — Oracle"
]

cert_html = "".join([f'<span class="cert-badge">{cert}</span> ' for cert in certs])
st.markdown(f'<div class="cert-grid">{cert_html}</div>', unsafe_allow_html=True)

st.markdown("---")

# --- EDUCATION ---
st.markdown('<div class="section-title">✦ Education</div>', unsafe_allow_html=True)
st.markdown("""
<div class="edu-card">
    <h3>B.Sc. Computer Science</h3>
    <div class="uni">Swami Ramanand Teerth Marathwada University (SRTMU), Nanded</div>
    <div class="gpa">GPA: 9.1 / 10</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div class="footer">
    © 2026 Aleena Anam · Built with ❤️ using Streamlit · 
    <a href="mailto:anamaleena0@gmail.com">Get in touch</a>
</div>
""", unsafe_allow_html=True)
