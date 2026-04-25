# Piyush Kulkarni — Portfolio

A god-level Flask portfolio with flip cards, animations, and a full shayari section.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```
Visit: http://localhost:5000

## ☁️ Deploy FREE on Render.com

1. Push this folder to GitHub
2. Go to https://render.com → Sign up free
3. New → Web Service → Connect your GitHub repo
4. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: **Free**
5. Click Deploy → Done! 🎉

Your site will be live at: `https://your-app-name.onrender.com`

## ✏️ Customize

Edit `templates/index.html`:
- Replace placeholder info (email, phone, city)
- Add your own shayaries in the `shayaris` array (line ~340)
- Add your projects in the Projects section
- Add your photo by replacing the emoji in `.hero-img-inner` with an `<img>` tag

## 📁 Structure
```
portfolio/
├── app.py              # Flask app
├── requirements.txt    # Dependencies
├── Procfile           # For deployment
├── render.yaml        # Render config
└── templates/
    └── index.html     # Your entire portfolio
```
