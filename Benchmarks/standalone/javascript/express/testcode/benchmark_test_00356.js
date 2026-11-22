// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00356(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  appDb.prepare("SELECT id, name FROM users ORDER BY " + orderColumn).all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00356 };
