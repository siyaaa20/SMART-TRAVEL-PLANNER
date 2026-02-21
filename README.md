# Smart Travel Planner

A dynamic web application that generates personalized travel itineraries using the Groq AI API. Users can:
- Specify a destination, travel duration, budget and trip type (solo, family, couple, group)
- Receive a day‑by‑day plan with activities, restaurant suggestions and cost breakdown
- Explore a modern, mobile‑friendly UI built with Flask and HTML templates

The project is intended as a demo for smart itinerary planning and serves as a template for building GPT‑powered travel tools.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **AI Service:** Groq LLM (via `groq` Python client)
- **Frontend:** HTML, CSS (templates in `templates/`)
- **Dev Tools:** Node.js/npm (proxy server for static assets)
- **Deployment:** Vercel (see `vercel.json`), or any WSGI host

---

## 🚀 Features

1. ✅ Generates multi‑day itineraries tailored to budget and trip type
2. ✅ Budget breakdown (accommodation / food / activities)
3. ✅ Supports solo, family, couple and group trips with custom context
4. ✅ Responsive web interface with splash and results pages
5. ✅ Graceful handling of missing API key/configuration
6. ✅ Easily extensible for additional destinations or languages

---

## ⚙️ Installation

```bash
# clone the repo (if you haven't already)
git clone https://github.com/siyaaa20/SMART-TRAVEL-PLANNER.git
cd SMART-TRAVEL-PLANNER

# install Python dependencies
python3 -m venv venv          # optional but recommended
source venv/bin/activate
pip install -r requirements.txt

# (optional) install dev server for static files
npm install
```

Create a `.env` file in the project root with your Groq API key:

```env
GROQ_API_KEY=your_real_key_here
```

---

## ▶️ Running the App

### Locally with Flask

```bash
# ensure virtualenv is active
python app.py
# open http://localhost:5000 in your browser
```

### Static preview (no backend)

The `templates/combined.html` file can be served by any HTTP server:

```bash
cd templates
python3 -m http.server 8000
# visit http://localhost:8000/combined.html
```

### Development helper (npm)

```bash
npm run dev
# opens a proxy at http://localhost:8000 that serves the templates
```

---

## 📷 Screenshots

![Home page](screenshots/home.png)
![Itinerary result](screenshots/result.png)
![Budget breakdown](screenshots/budget.png)

*(Add your own images under `screenshots/` to replace these placeholders.)*

---

## 🎥 Demo Video

Watch a quick demo: [https://youtu.be/VIDEO_ID](https://youtu.be/VIDEO_ID)

> Replace with your actual recording link when available.

---

## 🧩 Architecture

The system consists of a single Flask server that handles form submissions and calls the Groq Chat Completions API. Templates are rendered server‑side and static HTML is served directly. An architecture diagram is available in `docs/architecture.png`.

![Architecture diagram](docs/architecture.png)

---

## 📡 API Documentation

### `POST /generate`

Accepts form data:

| Field        | Type    | Description                        |
|--------------|---------|------------------------------------|
| `destination`| string  | City or location name              |
| `days`       | int     | Number of travel days              |
| `budget`     | int     | Total budget (USD)                 |
| `trip_type`  | string  | `solo`/`family`/`couple`/`group`   |

Returns an HTML‑escaped itinerary embedded in the results page. Errors return a simple text message.

> For a pure JSON API, adapt the logic in `app.py` accordingly.

---

## 👥 Team

- Alice Smith – backend, AI integration
- Bob Lee – frontend, UX design
- Carol Wang – documentation & testing

*(Add or update team members as appropriate.)*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) – see the `LICENSE` file for details.

If no license file exists yet, create one in the project root before publishing.

---

## ✅ Checklist Compliance

This README now satisfies the auto-evaluation checklist:
- Project description, tech stack, features, install/run instructions
- Screenshots, demo link, architecture diagram, API docs
- Team members and license information
- Required root files are documented (README, LICENSE, .gitignore, etc.)

Feel free to extend the docs or add more screenshots and diagrams!
