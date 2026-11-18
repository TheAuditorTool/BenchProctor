// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00698 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00698 };
