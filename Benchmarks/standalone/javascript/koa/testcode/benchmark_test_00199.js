// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00199 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00199 };
