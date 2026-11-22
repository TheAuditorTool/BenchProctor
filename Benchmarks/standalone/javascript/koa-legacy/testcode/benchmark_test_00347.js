// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00347 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00347 };
