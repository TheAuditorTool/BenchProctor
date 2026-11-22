// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00022 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = decodeURIComponent(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00022 };
