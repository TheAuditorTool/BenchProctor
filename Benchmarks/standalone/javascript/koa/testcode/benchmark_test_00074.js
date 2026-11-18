// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00074 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = `${userInput}`;
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00074 };
