// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00041 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00041 };
