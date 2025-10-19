// import "./globals.css"; // only if you have one
import React from "react";

export const metadata = {
  title: "AI Ads Frontend",
  description: "Frontend for the AI Ads project",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
