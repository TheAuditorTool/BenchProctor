// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00270 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00270 };
