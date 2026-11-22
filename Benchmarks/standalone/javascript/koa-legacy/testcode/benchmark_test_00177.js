// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00177 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00177 };
