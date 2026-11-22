// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00245(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + data + "'").all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00245 };
