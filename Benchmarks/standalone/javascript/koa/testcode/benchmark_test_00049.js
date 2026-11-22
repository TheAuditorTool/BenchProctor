// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00049 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { ctx.status = 400; ctx.body = { error: "not an email address" }; return; }
  const domain = emailMatch[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00049 };
