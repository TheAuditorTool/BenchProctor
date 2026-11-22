// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00218 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00218 };
