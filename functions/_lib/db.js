// Akses D1. Tabel dibuat otomatis (CREATE TABLE IF NOT EXISTS), jadi tidak perlu menjalankan migrasi manual.
import { HttpError } from "./http.js";

const ready = new WeakSet();

export async function getDb(env) {
  if (!env.DB) {
    throw new HttpError(503, "Database D1 belum terpasang. Ikuti langkah di SETUP-ADMIN.md (binding DB).", { setup: "db" });
  }
  if (!ready.has(env.DB)) {
    await env.DB.batch([
      env.DB.prepare("CREATE TABLE IF NOT EXISTS cms (key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at TEXT NOT NULL)"),
      env.DB.prepare("CREATE TABLE IF NOT EXISTS login_fail (ip TEXT PRIMARY KEY, count INTEGER NOT NULL, first_at INTEGER NOT NULL)"),
    ]);
    ready.add(env.DB);
  }
  return env.DB;
}

export async function getDoc(db, key) {
  const row = await db.prepare("SELECT value, updated_at FROM cms WHERE key = ?").bind(key).first();
  if (!row) return null;
  return { content: JSON.parse(row.value), updated_at: row.updated_at };
}

export async function putDoc(db, key, content) {
  const now = new Date().toISOString();
  await db
    .prepare("INSERT INTO cms (key, value, updated_at) VALUES (?, ?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at")
    .bind(key, JSON.stringify(content), now)
    .run();
  return now;
}
