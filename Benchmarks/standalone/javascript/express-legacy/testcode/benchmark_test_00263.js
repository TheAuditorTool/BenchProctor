// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00263(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00263 };
