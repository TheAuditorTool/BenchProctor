// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00677 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(userInput) };
}

module.exports = { BenchmarkTest00677 };
