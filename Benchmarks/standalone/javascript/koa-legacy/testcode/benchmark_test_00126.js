// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00126 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  ctx.cookies.set("session", userInput, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00126 };
