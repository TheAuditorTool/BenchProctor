// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00257 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00257 };
