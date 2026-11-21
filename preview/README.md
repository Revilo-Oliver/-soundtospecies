Preview site: static mock of the user-facing UI.

To view locally:

1. Open a terminal in the preview folder:
   cd "c:\Users\olive\OneDrive\ドキュメント\SoundToSpecies\preview"
2. Start a simple static server:
   python -m http.server 8001
3. Open http://127.0.0.1:8001/ in your browser

This is a static preview only — forms are non-functional. Use the live Django app for real auth and uploads.
