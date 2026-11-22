// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00151 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const emailMatch = String(userInput).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { ctx.status = 400; ctx.body = { error: "not an email address" }; return; }
  const domain = emailMatch[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00151 };
