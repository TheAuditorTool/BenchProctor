// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00550 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00550 };
