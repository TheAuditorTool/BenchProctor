// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00146(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + userInput + "'").all();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00146 };
