// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00061 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + data + "'").all();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00061 };
