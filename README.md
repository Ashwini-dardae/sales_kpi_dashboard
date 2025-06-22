# sales_kpi_dashboard
Built a dynamic and interactive Sales KPI Dashboard using Streamlit, which visualizes key business metrics like Revenue, Orders, CAC (Customer Acquisition Cost), and AOV (Average Order Value). The app integrates forecasting using Linear Regression and enables natural language querying of the dataset using LangChain + Groq's LLama3 model.

🚀 Features
✅ KPI Dashboard
Track and display core business metrics like:

💰 Revenue

🛒 Orders

👥 Customers

📈 CAC (Customer Acquisition Cost)

💵 AOV (Average Order Value)

🔮 Forecasting Engine
Uses Linear Regression to predict next month's revenue based on past trends.
🤖 GenAI Integration (LangChain + Groq)
Ask natural language questions like “What was the revenue for Face Wash?”

Get smart summaries of sales data with one click.

🧠 Memory-based LLM Interaction
Built-in memory support allows the chatbot to remember context and give personalized responses.
🧱 Tech Stack
Layer	Tools Used
📊 UI/Frontend	Streamlit
📦 Data Manipulation	Pandas
🔍 Forecasting	scikit-learn (Linear Regression)
🤖 GenAI	LangChain, Groq (LLama3-70B)
🌐 Backend Logic	Python
📁 Others	dotenv, langchain-groq

📁 Folder Structure
.
├── app.py                    # Streamlit frontend app
├── kpi_utils.py             # KPI calculation logic
├── forecast_utils.py        # Revenue forecasting model
├── genai_utils.py           # LangChain + Groq LLM logic
├── data/
│   └── sales_data.csv       # Sample sales data
├── requirements.txt         # Python dependencies
└── README.md                # You're reading this!

📈 KPIs Calculated
Total Revenue = sum of all revenue entries

Orders = total orders across products

CAC = Total Ad Spend / Total Customers

AOV = Revenue / Orders

🧠 Sample Prompts for GenAI
- "What's the total revenue for January?"
- "Which product generated the highest orders?"
- "Summarize the sales data for me"
- "What is the CAC for Skincare category?"


