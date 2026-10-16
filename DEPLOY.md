# Vercel Deployment Steps

1. Free Postgres உருவாக்குங்க (Neon அல்லது Supabase) -> connection string copy பண்ணுங்க.
   Password-ல special character இருந்தா URL-encode பண்ணணும் (@ -> %40, # -> %23).
2. Local-ல (PowerShell) tables + login user உருவாக்குங்க:
   $env:DATABASE_URL="postgresql://USER:PASS@HOST:5432/DBNAME"
   python manage.py migrate
   python manage.py createsuperuser
3. Vercel -> Settings -> Environment Variables (Production):
   DATABASE_URL = (same string, quotes இல்லாம)
   SECRET_KEY   = (ஏதாவது நீளமான random string)
4. staticfiles/ folder-ஐ git-ல commit பண்ணணும் (.gitignore-ல போடாதீங்க).
   CSS மாத்தினா: python manage.py collectstatic --noinput
5. vercel --prod
