// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00086 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const token = crypto.randomInt(2 ** 47).toString(36) + crypto.randomInt(2 ** 47).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00086 };
