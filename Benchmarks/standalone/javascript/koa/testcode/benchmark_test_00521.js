// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00521 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const [data] = String(userInput).split(',');
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00521 };
