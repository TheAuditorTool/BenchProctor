// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00316 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00316 };
