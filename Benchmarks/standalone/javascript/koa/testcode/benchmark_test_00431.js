// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00431 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = Buffer.from(userInput, "hex").toString();
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00431 };
