// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00660 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = `${userInput}`;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00660 };
