// SPDX-License-Identifier: Apache-2.0
const zod = require("zod");

const BenchmarkTest00002 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).slice(0, 200);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00002 };
