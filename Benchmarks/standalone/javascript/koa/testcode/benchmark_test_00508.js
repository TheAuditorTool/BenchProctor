// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00508 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = userInput != null ? userInput : '';
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00508 };
