# AI-Powered HR Automation: Transforming Entire Department Workflows

## **Project Overview**

You've built a comprehensive HR AI system that combines **Machine Learning models** with **AI agents** to automate HR tasks like candidate screening, job matching, and salary prediction.

![System Diagram](https://screendy-cdn.fra1.cdn.digitaloceanspaces.com/platfrom-v2/_files/file_1758053485392_diagram.png)

---

## 🧠 **Machine Learning Models (4 Models)**

### 1. **Job Fit Prediction Model**
- **Purpose**: Determines if a candidate is a good fit for a specific job  
- **Input**: Required skills, candidate skills, degree, years of experience  
- **Output**: Probability score (0-1) and binary fit decision  
- **Algorithm**: Logistic Regression with TF-IDF skill matching  
- **Use Case**: “Is this candidate suitable for our DevOps position?”

### 2. **Salary Prediction Model**
- **Purpose**: Predicts competitive salary for a role  
- **Input**: Years of experience, role, degree, company size, location, level  
- **Output**: Predicted salary amount (in MAD)  
- **Algorithm**: Linear Regression with categorical encoding  
- **Use Case**: “What salary should we offer this ML Engineer?”

### 3. **Resume Screening Model**
- **Purpose**: Decides if a resume should advance to interview stage  
- **Input**: Resume text, job description text  
- **Output**: Advancement probability and binary decision  
- **Algorithm**: Deep Learning (Neural Network) with TF-IDF  
- **Use Case**: “Should we interview this candidate based on their resume?”

### 4. **Candidate Priority Model**
- **Purpose**: Ranks candidates by hiring priority  
- **Input**: Experience band, skills coverage, referral flag, English level, location match  
- **Output**: Priority level (High/Medium/Low) with confidence  
- **Algorithm**: Random Forest Classifier  
- **Use Case**: “Which candidates should we interview first?”

> [**Dataset**](https://github.com/MohamedMeksi/Dataset-genAI)

---

## 🚀 **API Endpoints (Flask Backend)**

### **Direct Model Access**
```javascript
POST /api/salary/predict
POST /api/job_fit/predict
POST /api/resume_screen/predict
POST /api/candidate_priority/predict
```

### **Example API Call**
```json
POST /api/salary/predict
{
  "years_experience": 5,
  "role": "Data Scientist",
  "degree": "Masters",
  "company_size": "Large",
  "location": "Casablanca",
  "level": "Senior"
}

Response: {"predicted_salary": 28500}
```

---

## 🤖 **AI Agent System**

### **Simple HR AI Agent Features**
- **Conversational Interface**: Natural language questions → AI responses  
- **Tool Integration**: 8 specialized HR tools  
- **ML Model Integration**: Uses all 4 models automatically  
- **Database Integration**: MongoDB with candidate/job data  

### **Available Tools**
1. `get_candidate` – Get candidate information  
2. `get_job` – Get job information  
3. `check_job_fit` – ML-powered job fit analysis  
4. `predict_salary` – Salary prediction  
5. `screen_resume` – Resume screening  
6. `get_priority` – Candidate priority level  
7. `list_candidates` – Show all candidates  
8. `list_jobs` – Show all jobs  

---

## 💬 **How Students Can Use It**

### **1. Direct API Testing**
```bash
# Test salary prediction
curl -X POST http://localhost:8000/api/salary/predict \
  -H "Content-Type: application/json" \
  -d '{"years_experience": 3, "role": "Frontend Developer"}'
```

### **2. AI Agent Conversations**
```bash
python run.py
# Then ask: "Is CAND001 a good fit for job JOB001?"
```

### **3. Example Student Questions**
- "What salary should we offer a Senior DevOps Engineer?"  
- "Should we advance this candidate's resume?"  
- "Which candidate has the highest priority?"  
- "Show me all available candidates"  

---

## 📊 **Dataset Structure**

### **Candidates Collection (8 candidates)**
```json
{
  "candidate_id": "CAND001",
  "name": "Ahmed El Mansouri",
  "current_role": "DevOps Engineer",
  "years_experience": 6.5,
  "skills": "Docker, Kubernetes, AWS, Linux",
  "degree": "Masters"
}
```

### **Jobs Collection (6 jobs)**
```json
{
  "job_id": "JOB001",
  "title": "Senior DevOps Engineer",
  "company": "TechCorp Morocco",
  "location": "Casablanca",
  "required_skills": "Docker, Kubernetes, AWS, Linux"
}
```

---

## 🛠 **Technical Architecture**

```javascript
User Question → GPT-4 → Tool Selection → ML Models → Database → Response
```

### **Key Components**
- **Frontend**: Conversational chat interface, CLI  
- **AI Engine**: OpenAI GPT-4 for natural language processing  
- **Tools Layer**: 8 specialized HR functions  
- **ML Layer**: 4 prediction models  
- **Data Layer**: MongoDB with HR data  
- **API Layer**: Direct REST endpoints  
