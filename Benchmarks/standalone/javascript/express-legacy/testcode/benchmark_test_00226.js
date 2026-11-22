// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00226(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + parsedId + "'").all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00226 };
