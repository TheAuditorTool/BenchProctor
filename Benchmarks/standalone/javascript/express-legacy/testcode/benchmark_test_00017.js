// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00017(req, res) {
  const userInput = req.body.field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + data + "'").all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00017 };
