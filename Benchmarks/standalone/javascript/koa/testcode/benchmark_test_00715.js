// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00715 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  ctx.cookies.set("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00715 };
