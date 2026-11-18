// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const zod = require("zod");

const BenchmarkTest00002 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = `${userInput}`;
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00002 };
