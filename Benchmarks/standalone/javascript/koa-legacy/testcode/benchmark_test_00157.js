// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00157 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { ctx.status = 400; ctx.body = { error: "not an email address" }; return; }
  const domain = emailMatch[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00157 };
