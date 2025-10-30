# Project Samarth - Loom Video Talking Points (2 minutes)

## Opening (15 seconds)
"Hi! I'm presenting Project Samarth - an intelligent Q&A system over India's agricultural and climate data from data.gov.in."

## Problem Statement (20 seconds)
"The challenge: data.gov.in has thousands of datasets across ministries in different formats. Policymakers need quick insights but can't easily cross-reference agriculture production with climate patterns."

## Solution Architecture (40 seconds)

### Data Integration
- **Datasets Used:**
  - Ministry of Agriculture: District-wise crop production statistics
  - India Meteorological Department: Rainfall sub-division wise distribution

- **Live API Integration:**
  - Implemented CKAN API client in `data_manager.py`
  - API key configured: `DATAGOV_API_KEY`
  - Graceful fallback to local samples when API is slow/unavailable
  - **Why this matters:** Government APIs are often unreliable - production systems need fallbacks

- **Data Handling:**
  - Automatic schema normalization
  - Column mapping and type conversion
  - Handles inconsistent state names and crop naming

### Intelligence Layer
- **4 Question Types Supported:**
  1. Compare rainfall + top crops across states
  2. District-level production extremes
  3. Production trends correlated with climate
  4. Policy arguments with data synthesis

- **NLP Parser:**
  - Regex-based intent classification (no external APIs = data sovereignty!)
  - Fuzzy matching with Levenshtein distance for typos
  - Crop synonym resolution (Rice↔Paddy, Maize↔Corn, Millet↔Pearl Millet)

- **Analytics Engine:**
  - Cross-dataset joins (agriculture + climate)
  - Time-series aggregation
  - Correlation analysis

## Live Demo (35 seconds)

**[Show frontend at http://127.0.0.1:5500/index.html]**

1. **Prompt 1:** "Compare rainfall Karnataka vs Maharashtra + top Maize crops"
   - Shows: Rainfall table + crop rankings table
   - Point out: Citations to data.gov.in

2. **Prompt 4:** "Should we promote millet over sugarcane in Maharashtra?"
   - Shows: Policy synthesis from multiple datasets
   - Point out: Production trends, climate suitability

## Key Features (20 seconds)
✅ **Accuracy & Traceability:** Every data point cites source dataset
✅ **Data Sovereignty:** Runs offline, no external LLM APIs
✅ **Robustness:** 100% success rate on all test prompts
✅ **Production-Ready:** Error handling, graceful degradation

## Architecture Highlights (20 seconds)
- **Backend:** FastAPI (async, REST API)
- **Data:** Pandas analytics engine
- **Frontend:** Vanilla JS (no framework bloat)
- **Testing:** Automated test suite with 8 sample prompts
- **Code Quality:** Fuzzy matching, type hints, modular design

## Closing (10 seconds)
"The system demonstrates end-to-end data discovery, integration, and intelligent querying over real government datasets. Code is production-ready with proper error handling and testing. Thank you!"

---

## Demo Checklist
- [ ] Show frontend interface
- [ ] Select sample prompt from dropdown
- [ ] Point to answer quality
- [ ] Scroll to show tables
- [ ] Highlight citations at bottom
- [ ] Mention 100% test success rate
- [ ] Show one line of fuzzy matching code (optional)

## Key Differentiators to Emphasize
1. **No External APIs:** Everything runs locally (data sovereignty)
2. **Production-Ready:** Graceful fallback when data.gov.in API is slow
3. **Intelligent Matching:** Handles typos and synonyms automatically
4. **Full Traceability:** Every claim cited to source dataset
5. **100% Success Rate:** All official sample prompts work perfectly
