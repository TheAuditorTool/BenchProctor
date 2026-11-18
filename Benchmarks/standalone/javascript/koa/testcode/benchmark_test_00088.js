// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00088 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00088 };
