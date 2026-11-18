// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00328 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00328 };
