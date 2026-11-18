// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00426 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00426 };
