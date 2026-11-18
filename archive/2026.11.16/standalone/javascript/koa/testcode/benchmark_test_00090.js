// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00090 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  ctx.cookies.set("session", userInput, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00090 };
