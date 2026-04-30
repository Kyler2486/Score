# ScoreLab — MusicXML Tools

A Flask/Python web app for working with MusicXML files. Includes user accounts, 20+ music tools, an extensions store, an admin panel, a collapsible sidebar, dark/light theme, and hidden Easter eggs.

## Running the App

```bash
python3 main.py
```

Runs on port 5000.

## Project Structure

```
main.py                         ← Entry point (create_app, init_db, run)
scorelab/
├── __init__.py
├── app.py                      ← Flask app factory, registers blueprints
├── models.py                   ← DB helpers, User class, seed_admin, load_user
├── music_utils.py              ← parse_musicxml, transpose, metadata, note_stats, analyze_form
├── templates/
│   ├── shell.py                ← BASE_CSS, SIDEBAR_JS, EASTER_EGG_JS, make_shell(), nav_ctx()
│   ├── tools_content.py        ← AUTH_CSS, AUTH_TEMPLATE, CONVERTER, MXL, META, TRANSPOSE, STATS, BPM
│   ├── tools_content2.py       ← METRONOME, VIEWER, INTERVAL, CHORD, SETTINGS, PROFILE, TUNER, OSCOPE
│   ├── extensions_content.py   ← LANDING_TEMPLATE, EXTENSIONS_CONTENT, all EXT_* strings
│   └── admin_content.py        ← BANNED_TEMPLATE, ADMIN_CSS, ADMIN_CONTENT
└── routes/
    ├── __init__.py
    ├── auth.py                 ← /login, /register, /logout, /landing  [auth blueprint]
    ├── main.py                 ← /, /convert, /tools/*, /api/presets, /profile/*, /admin  [main blueprint]
    ├── extensions_store.py     ← /extensions store page  [ext_store blueprint]
    └── extensions.py           ← all /ext/* routes  [ext blueprint]
static/
├── avatars/                    ← uploaded user avatars
└── banners/                    ← uploaded user banners
users.db                        ← SQLite database
```

## Tools (sidebar navigation)

| Route | Tool |
|-------|------|
| `/` | **MusicXML → Text** — drag-and-drop, convert to plain text for AI |
| `/tools/mxl` | **MXL → XML** — decompress .mxl archives to plain .xml |
| `/tools/metadata` | **Metadata Viewer** — title, composer, tempo, key, parts |
| `/tools/transpose` | **Transpose** — shift all notes ±N semitones, download result |
| `/tools/stats` | **Note Statistics** — note frequency bar charts, duration breakdown |
| `/tools/bpm` | **BPM Tapper** — tap or press Space/Enter to calculate live BPM |
| `/tools/metronome` | **Metronome** — audio metronome with presets, 8 sounds, flash mode |
| `/tools/viewer` | **Sheet Music Viewer** — render MusicXML in the browser |
| `/tools/interval` | **Interval Trainer** — interactive interval recognition |
| `/tools/chord` | **Chord Reference** — chord diagrams and playback |
| `/tools/tuner` | **Chromatic Tuner** — mic-based pitch detection |
| `/tools/oscilloscope` | **Oscilloscope** — real-time waveform visualizer |
| `/extensions` | **Extensions Store** — install/uninstall sidebar extensions |

## Extensions (/ext/*)

Scale Finder, Circle of Fifths, Pitch Detector, Rhythm Trainer, Ear Training, Notation Guide, Frequency Calculator, Time Sig Trainer, Chord Progressions, Solfège Trainer, Form Analyzer, Piano Keyboard, Visual Metronome, Music Theory Quiz, Tempo Converter, MIDI Player, Guitar Tuner, Drum Machine, Arpeggiator, Music Flashcards, Note Reading

## Layout

- **Top nav** with hamburger toggle (☰)
- **Collapsible sidebar** (240px) with Tools / Extensions / Account sections
- Sidebar state persisted in `localStorage`
- Dark/light theme via CSS custom properties + `localStorage`

## User Accounts & Admin

- Email + username (unique), display name (non-unique), avatar, banner
- Admin panel at `/admin` — ban/unban, grant/revoke admin, delete accounts
- Ban check on every request — banned users see a dedicated ban page
- Admin seeding via environment variables: `ADMIN_EMAIL`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`

## Easter Eggs

1. **Konami code** (↑↑↓↓←→←→BA) → animated note rain
2. **Logo ×5 clicks** → disco mode
3. **Logo double-click** → Matrix music rain
4. **Avatar ×7 clicks** → spinning animation
5. **Type "music"** → hint toast
6. **Type "clef"** → clef symbol rain
7. **`/secret` page** → secret achievement page
8. **Pachelbel filename** → gold achievement banner on converter
9. **88 notes** → piano achievement on converter
10. **45s idle** on home page → random Easter egg hint

## Key Dependencies

- flask
- flask-login
- werkzeug
- xml.etree.ElementTree (stdlib)
- zipfile (stdlib)
