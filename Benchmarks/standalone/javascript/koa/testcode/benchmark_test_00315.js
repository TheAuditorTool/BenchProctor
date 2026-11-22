// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00315 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  appDb.prepare("SELECT id, name FROM users ORDER BY " + orderColumn).all();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00315 };
