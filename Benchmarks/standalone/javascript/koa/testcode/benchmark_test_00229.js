// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00229 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00229 };
