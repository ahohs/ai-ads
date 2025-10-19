```markdown
# 🧠 AI Ads – Full Stack App (FastAPI + Next.js)

A modern full-stack boilerplate for AI Ads projects — powered by **FastAPI** (backend) and **Next.js** (frontend), running in Docker for easy local development.

---

## 🚀 Project Structure

```

ai-ads/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── routes/
│   │   │   └── offers.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── tsconfig.json
│
├── ops/
│   ├── docker-compose.dev.yml
│   ├── backend.Dockerfile
│   └── frontend.Dockerfile
│
└── README.md

````

---

## 🐳 Local Development with Docker

### 1️⃣ Build and start the stack

From the **ops/** folder:
```bash
docker compose -f docker-compose.dev.yml up --build
````

This will:

* Build and start **FastAPI backend** on port `8000`
* Build and start **Next.js frontend** on port `3000`
* Watch for live code changes in both

---

### 2️⃣ Access the running containers

| Service     | URL                                                                  | Description                   |
| ----------- | -------------------------------------------------------------------- | ----------------------------- |
| 🧠 Backend  | [http://localhost:8000](http://localhost:8000)                       | FastAPI root endpoint         |
| ❤️ Health   | [http://localhost:8000/api/health](http://localhost:8000/api/health) | Health check JSON             |
| 🌐 Frontend | [http://localhost:3000](http://localhost:3000)                       | Next.js UI (Docker container) |

---

### 3️⃣ Verify containers

List all running containers:

```bash
docker ps
```

You should see something like:

```
CONTAINER ID   IMAGE              COMMAND                  PORTS
abcd1234       ops-backend        "bash -lc 'uvicorn…"     0.0.0.0:8000->8000/tcp
efgh5678       ops-frontend       "npm run dev"            0.0.0.0:3000->3000/tcp
```

View logs in real-time:

```bash
docker compose -f docker-compose.dev.yml logs -f
```

Stop all containers:

```bash
docker compose -f docker-compose.dev.yml down
```

Clean up everything (containers + volumes):

```bash
docker compose down -v
```

---

## 🧩 Notes

* **Frontend Framework:** Next.js 14 (TypeScript + App Router)
* **Backend Framework:** FastAPI + Uvicorn
* **Hot Reload:** Enabled for both via volume mounting
* **Backend Health Endpoint:** `/api/health` returns `{ "status": "ok" }`
* **Frontend Default Page:** Displays a simple message and link to the backend health check.

---

## 🛠 Common Issues

### ❌ `Module not found: './globals.css'`

→ Create the file `frontend/app/globals.css` or remove the import line in `layout.tsx`.

### ❌ `Error: The default export is not a React Component`

→ Ensure your `frontend/app/page.tsx` exports a function component like:

```tsx
export default function Page() {
  return <h1>Hello World</h1>;
}
```

### ❌ Docker build fails (network error)

→ Run:

```bash
npm cache clean --force
```

and retry the build.

---

## ✅ Next Steps

* Add API routes in `backend/app/routes/`
* Connect the frontend to backend data using `fetch()` from `http://localhost:8000/api/...`
* Deploy using production Docker Compose or Kubernetes (coming soon)