// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00317 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  Object.assign(ctx.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00317 };
