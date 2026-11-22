// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00248 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = `${userInput}`;
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00248 };
