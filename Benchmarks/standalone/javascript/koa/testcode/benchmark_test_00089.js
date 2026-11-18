// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00089 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00089 };
