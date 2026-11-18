// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00621 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(userInput) };
}

module.exports = { BenchmarkTest00621 };
