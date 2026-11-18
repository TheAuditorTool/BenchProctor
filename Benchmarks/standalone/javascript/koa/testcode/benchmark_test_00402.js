// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00402 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = `${userInput}`;
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00402 };
