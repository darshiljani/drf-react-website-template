import react from '@vitejs/plugin-react'
import path from 'path'
import { defineConfig, loadEnv } from 'vite'
import tsconfigPaths from 'vite-tsconfig-paths'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.

  const env = loadEnv(mode, process.cwd(), '')
  return {
    plugins: [react(), tsconfigPaths()],
    server: {
      hmr: { port: 51730 },
      host: '0.0.0.0',
      port: 5173,
      open: false, // Set this to true to open project in browser on starting server
      strictPort: true, // Set this to false to allow using ports other than 5173
    },
    define: {
      'process.env': JSON.stringify(env),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
    test: {
      globals: true,
      environment: 'jsdom',
      setupFiles: './vitest.setup.js',
    },
  }
})
