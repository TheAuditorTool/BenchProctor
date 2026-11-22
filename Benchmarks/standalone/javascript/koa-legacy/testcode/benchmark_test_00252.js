// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00252 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = '" + parsedId + "'").all();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00252 };
