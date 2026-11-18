// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00085 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00085 };
