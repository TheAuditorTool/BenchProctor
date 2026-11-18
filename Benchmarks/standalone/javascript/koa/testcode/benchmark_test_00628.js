// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00628 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = decodeURIComponent(userInput);
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00628 };
