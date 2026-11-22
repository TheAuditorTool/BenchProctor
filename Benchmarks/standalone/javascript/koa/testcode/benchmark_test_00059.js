// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00059 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = String(userInput).slice(0, 200);
  const token = crypto.randomInt(2 ** 47).toString(36) + crypto.randomInt(2 ** 47).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00059 };
