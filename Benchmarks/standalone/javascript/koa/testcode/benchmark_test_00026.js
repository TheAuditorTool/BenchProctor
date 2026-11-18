// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00026 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00026 };
