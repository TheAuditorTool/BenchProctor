// SPDX-License-Identifier: Apache-2.0
const zod = require("zod");

const BenchmarkTest00548 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00548 };
