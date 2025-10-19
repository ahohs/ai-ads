"use client";

import React from "react";

export default function Page() {
  return (
    <main style={{ fontFamily: "sans-serif", padding: "2rem" }}>
      <h1>🚀 AI Ads Frontend is running!</h1>
      <p>
        Backend API:{" "}
        <a href="http://localhost:8000/api/health" target="_blank">
          Check Health
        </a>
      </p>
    </main>
  );
}
