// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00251 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  appDb.prepare("SELECT id, name FROM users WHERE name = ?").all(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00251 };
