// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00181 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.app.context.announcement = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00181 };
