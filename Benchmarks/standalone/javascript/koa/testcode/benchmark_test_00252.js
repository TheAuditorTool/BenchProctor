// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00252 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const Database = require("better-sqlite3");
  const appDb = (globalThis._appDb ??= new Database("/var/app/data/app.db", { readonly: true }));
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  appDb.prepare("SELECT id, name FROM users ORDER BY " + orderColumn).all();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00252 };
