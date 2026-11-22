// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00319(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00319 };
