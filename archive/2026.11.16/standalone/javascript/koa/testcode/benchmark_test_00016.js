// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00016 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = `${userInput}`;
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00016 };
