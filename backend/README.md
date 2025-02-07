# Smart Match

## Description

The **Smart match** is a job-matching platform designed to connect job seekers with relevant job offers. The system uses AI-powered algorithms to analyze job seekers' profiles and match them with job offers based on criteria like domain, technical skills, job type (remote, hybrid, or part-time), and years of experience. The platform also provides personalized improvement suggestions to help job seekers better align with the job market.

### Features:

- match scoring for each job offer
- Provide advice on improving job seekers' profiles based on their match results.

### match scoring algorithm details :

1. Embed the data: Concatenate skills, type of offer, and years of experience to create unique embeddings for both the job seeker and job offer.
2. Vector Search: Use MongoDB’s vector search to find similar job offers based on the embeddings.
3. Pipeline: Implement a pipeline that first filters by domain, then calculates the similarity score using the embeddings.
4. Match Scoring: Return the job offer with the highest match score.

## Technologies Used:

- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **AI** : sentence-transformers, openai
- **Frontend**: Optional (could be extended with a frontend framework like React)
