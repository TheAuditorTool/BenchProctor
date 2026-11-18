// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00096 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00096 };
