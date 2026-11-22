// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00347 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  ctx.cookies.set("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00347 };
