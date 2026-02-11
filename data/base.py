st_style = """
           <style>
           @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap');
           
           /* Global font */
           html, body, [class*="css"] {
               font-family: 'DM Sans', system-ui, -apple-system, sans-serif !important;
           }
           div.block-container { padding-top: 2rem; padding-bottom: 2rem; }
           #MainMenu { visibility: hidden; }
           footer { visibility: hidden; }
           header { visibility: visible; }
           /* Sidebar background matches home */
           section[data-testid="stSidebar"] {
               background-color: transparent !important;
               border-right: none !important;
           }
           section[data-testid="stSidebar"] > div { padding-top: 0.5rem !important; }
           </style>
           """

# Sidebar brand (above input parameters): DiabAI
sidebar_credits = """
<div style="
    padding: 0.25rem 0.5rem 0.75rem;
    margin-bottom: 0.75rem;
    margin-top: 0;
    text-align: center;
    border-bottom: 1px solid rgba(46, 134, 193, 0.25);
">
    <span style="
        font-size: 1.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #29b5e8;
        font-family: 'DM Sans', system-ui, sans-serif;
    ">DiabAI</span>
</div>
"""

footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 0, 90, 0.1); /* Navy tone */
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #FFFFFF;  /* White text color */
    }
    .footer a {
        color: #FFD700;  /* Golden link color */
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        <p>Asan Zindagi | AmirAbbasi4923 <a href="https://github.com/AmirAbbasi4923/Azan_Zindagi_Diabetes_Prediction_App" target="_blank">GitHub</a></p>
    </div>
    """


# Top header: empty (tagline removed to avoid cutoff)
head_template = ""

# Footer section: logo centered above credits (used at bottom of page)
footer_with_logo_template = """
    <div style="
        margin-top: 4rem;
        padding: 2.5rem 1.5rem;
        text-align: center;
        background: linear-gradient(180deg, rgba(46, 134, 193, 0.06) 0%%, transparent 100%);
        border-top: 1px solid rgba(46, 134, 193, 0.15);
        border-radius: 12px 12px 0 0;
    ">
        <div style="margin-bottom: 1.25rem;">
            <img src="data:image/png;base64,{logo_base64}" style="height: 56px; width: auto; display: inline-block; vertical-align: middle; background: transparent; mix-blend-mode: normal;" alt="Logo" />
        </div>
        <div style="font-size: 0.9rem; color: #5D6D7E; font-family: 'DM Sans', system-ui, sans-serif;">
            <strong style="color: #2E86C1;">Asaan Zindagi</strong>
            <span style="margin: 0 0.35rem;">|</span>
            <a href="https://github.com/AmirAbbasi4923" target="_blank" style="color: #2E86C1; text-decoration: none;">Amir Abbasi</a>
            <span style="margin: 0 0.35rem;">|</span>
            <a href="https://github.com/Syed-Ammar-21" target="_blank" style="color: #2E86C1; text-decoration: none;">Syed Ammar</a>
        </div>
    </div>
    """

mrk = """
<div style="background-color: {}; 
color: white; 
margin-bottom: 50px;
padding: 10px;
max-width: 300px;
text-align: center;
border-radius: 5px;
font-family: 'DM Sans', system-ui, sans-serif;
font-weight: 500;">
    {}
</div>
"""


about_diabets = """
## What is diabetes?

**Diabetes** is a chronic health condition that affects how your body turns food into energy. It is characterized by high levels of glucose (sugar) in the blood, which occurs because the body either doesn’t produce enough insulin, doesn’t use insulin effectively, or both.

### **Types of Diabetes**:
1. **Type 1 Diabetes**:
   - An autoimmune condition where the immune system attacks and destroys insulin-producing cells in the pancreas.
   - Typically diagnosed in children and young adults.
   - Requires daily insulin injections to manage blood sugar.

2. **Type 2 Diabetes**:
   - The body becomes resistant to insulin, or the pancreas doesn’t produce enough insulin.
   - Often linked to lifestyle factors like obesity, physical inactivity, and poor diet, but genetics also play a role.
   - Managed through lifestyle changes, medications, and sometimes insulin.

3. **Gestational Diabetes**:
   - Occurs during pregnancy when the body cannot make enough insulin to support the increased demand.
   - Usually resolves after childbirth, but it increases the risk of developing type 2 diabetes later in life.

### **Symptoms of Diabetes**:
- Frequent urination
- Excessive thirst
- Extreme hunger
- Fatigue
- Blurred vision
- Slow-healing wounds
- Unexplained weight loss (especially in type 1 diabetes)

### **Complications of Untreated Diabetes**:
- Heart disease
- Kidney damage
- Vision loss (diabetic retinopathy)
- Nerve damage (diabetic neuropathy)
- Increased risk of infections

### **Management**:
- **Diet**: Eating a balanced diet, avoiding high-sugar foods.
- **Exercise**: Regular physical activity to improve insulin sensitivity.
- **Medications**: Insulin therapy or oral diabetes medications.
- **Monitoring**: Regularly checking blood glucose levels.
"""


warn = """
This project (model) was created for learning purposes, the model may make mistakes. Please trust only qualified experts.
"""