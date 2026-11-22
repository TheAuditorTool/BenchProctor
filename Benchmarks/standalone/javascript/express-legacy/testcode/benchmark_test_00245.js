// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00245(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + data + "'").all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00245 };
