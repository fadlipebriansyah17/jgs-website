-- Tabel Admin Dashboard. Catatan: functions/_lib/db.js membuat tabel ini otomatis (IF NOT EXISTS),
-- file ini hanya dokumentasi / untuk yang lebih suka menjalankan migrasi manual:
--   npx wrangler d1 execute jgs-db --remote --file=migrations/0002_admin_cms.sql
CREATE TABLE IF NOT EXISTS cms        (key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS login_fail (ip TEXT PRIMARY KEY, count INTEGER NOT NULL, first_at INTEGER NOT NULL);
