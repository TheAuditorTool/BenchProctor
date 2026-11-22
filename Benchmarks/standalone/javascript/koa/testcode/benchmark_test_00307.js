// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00307 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  new Function("return (" + String(processed) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00307 };
