# Vercel Deployment Guide

## Prerequisites
1. A [Vercel account](https://vercel.com)
2. [Vercel CLI](https://vercel.com/docs/cli)
3. A [Groq API key](https://console.groq.com/keys)

## Steps to Deploy

### 1. Set Up Environment Variables
Create a `.env.local` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI
```bash
vercel
```
Follow the prompts and add your `GROQ_API_KEY` when asked about environment variables.

#### Option B: Using Git (Recommended)
1. Push your code to GitHub
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "Add New..." → "Project"
4. Select your GitHub repository
5. Set environment variables:
   - `GROQ_API_KEY`: Your Groq API key
6. Click "Deploy"

### 3. Configure Environment Variables in Vercel
- Go to your project settings in Vercel Dashboard
- Navigate to "Environment Variables"
- Add `GROQ_API_KEY` with your Groq API key
- Save and redeploy

## Project Structure
```
.
├── api/
│   └── index.py          # Vercel serverless function wrapper
├── static/
│   └── style.css         # CSS styles
├── templates/
│   └── index.html        # HTML template
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── .vercelignore        # Files to exclude from Vercel
└── README.md            # This file
```

## Troubleshooting

### "GROQ_API_KEY not set" error
Make sure you've added the `GROQ_API_KEY` environment variable in your Vercel project settings.

### Static files not loading
Vercel will automatically serve files from the `static/` directory. Make sure your HTML references them correctly.

### Function timeout
If your requests are timing out, check that your Groq API key is valid and you have sufficient credits.

## Local Testing
Before deploying to Vercel, test locally:
```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.
