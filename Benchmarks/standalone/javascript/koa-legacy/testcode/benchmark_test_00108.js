// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00108 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = `${userInput}`;
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  Object.assign(ctx.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00108 };
