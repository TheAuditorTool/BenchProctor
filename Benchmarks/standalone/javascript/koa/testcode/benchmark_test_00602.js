// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

const BenchmarkTest00602 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00602 };
