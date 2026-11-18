// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00580 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = `${userInput}`;
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00580 };
