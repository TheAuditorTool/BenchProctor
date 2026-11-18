// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00679 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00679 };
