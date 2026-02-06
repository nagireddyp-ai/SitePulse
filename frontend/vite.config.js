import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/chat": "http://localhost:8000",
      "/incidents": "http://localhost:8000",
      "/generate-kb": "http://localhost:8000",
      "/dashboard-metrics": "http://localhost:8000",
      "/sync-servicenow": "http://localhost:8000",
      "/analyze-incident": "http://localhost:8000"
    }
  }
});
