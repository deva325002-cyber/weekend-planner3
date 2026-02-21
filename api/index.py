import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# For Vercel, the app is exported as 'app'
# The WSGI app is automatically handled by Vercel's Python runtime
