// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00394 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00394 };
