// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const nodeUtil = require("util");

const BenchmarkTest00285 = async (ctx) => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const data = nodeUtil.format("%s", userInput);
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00285 };
