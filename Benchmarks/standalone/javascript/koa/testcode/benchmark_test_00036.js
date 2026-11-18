// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00036 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00036 };
