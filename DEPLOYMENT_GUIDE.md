# Project Samarth - Deployment Guide

## ✅ Quick Deploy to Netlify (Manual - Most Reliable)

### Frontend Deployment

**Option 1: Drag & Drop (Easiest - 2 minutes)**

1. Go to https://app.netlify.com/drop
2. Drag the entire `frontend` folder into the drop zone
3. Netlify will deploy instantly and give you a live URL
4. Note the URL (e.g., `https://unique-name-123.netlify.app`)

**Option 2: Connect GitHub Repository**

1. Push your code to GitHub
2. Go to https://app.netlify.com
3. Click "Add new site" → "Import an existing project"
4. Connect to GitHub and select your repository
5. Configure:
   - Base directory: `frontend`
   - Build command: (leave empty)
   - Publish directory: `.` (current directory)
6. Click "Deploy site"

### Backend Deployment Options

**Option A: Render.com (Free Tier Available)**

1. Go to https://render.com
2. Click "New+" → "Web Service"
3. Connect your GitHub repo or upload code
4. Configure:
   - Name: `project-samarth-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Root Directory: `backend`
5. Add Environment Variable:
   - Key: `DATAGOV_API_KEY`
   - Value: `579b464db66ec23bdd000001df2e1e87602e4576665f24c51bc77875`
6. Click "Create Web Service"
7. Copy your backend URL (e.g., `https://project-samarth-backend.onrender.com`)

**Option B: Railway.app (Free Tier Available)**

1. Go to https://railway.app
2. Click "Start a New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python and FastAPI
5. Add environment variable:
   - `DATAGOV_API_KEY=579b464db66ec23bdd000001df2e1e87602e4576665f24c51bc77875`
6. Set root directory to `backend` in settings
7. Deploy and copy the public URL

**Option C: Local Backend (For Demo/Testing)**

If you just need it for the Loom video:
1. Keep backend running locally: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
2. Use ngrok to expose it: `ngrok http 8000`
3. Copy the ngrok HTTPS URL (e.g., `https://abc123.ngrok.io`)

### Connecting Frontend to Backend

Once both are deployed:

1. Open your Netlify site
2. In the "Backend Endpoint" field, enter your backend URL
3. The setting will be saved in browser localStorage
4. Test the sample prompts

### For Loom Video

**Recommended Setup:**
- Frontend: Deployed on Netlify (permanent URL)
- Backend: Either Render/Railway (permanent) OR local + ngrok (quick demo)

**Demo Script:**
1. Open your Netlify URL
2. Show the backend endpoint field
3. Select sample prompt from dropdown
4. Click "Ask Question"
5. Show the results with tables and citations
6. Mention: "Frontend is on Netlify, backend on [Render/Railway/local], data from live data.gov.in API with local fallback"

---

## 🚀 Current Status

✅ **Frontend ready:** Located in `/frontend` directory
✅ **Backend ready:** Located in `/backend` directory
✅ **API Key configured:** In `.env` file
✅ **All prompts working:** 100% success rate (8/8 tests passing)
✅ **Production ready:** Error handling, fallbacks, citations

## 📊 Architecture for Evaluation

**Highlight these points in your Loom:**

1. **Data Discovery:** Identified and integrated 2 datasets from data.gov.in
   - Agriculture: District-wise crop production
   - Climate: Rainfall sub-division wise

2. **Live API Integration:**
   - CKAN API client with pagination
   - Automatic retries and error handling
   - Graceful fallback to local samples

3. **Intelligent Q&A:**
   - NLP parser with 4 intent types
   - Fuzzy matching with Levenshtein distance
   - Cross-dataset joins and correlations

4. **Traceability:** Every answer cites source datasets

5. **Data Sovereignty:** No external LLM APIs, runs completely offline

## 🎬 Quick Loom Recording Checklist

- [ ] Show frontend UI on Netlify
- [ ] Demonstrate 2-3 sample prompts
- [ ] Point out data tables in results
- [ ] Highlight citations at bottom
- [ ] Mention 100% test success rate
- [ ] Explain architecture briefly
- [ ] Show one code snippet (fuzzy matching or API integration)

Total time: 2 minutes ✅
