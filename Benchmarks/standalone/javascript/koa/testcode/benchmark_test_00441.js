// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00441 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00441 };
