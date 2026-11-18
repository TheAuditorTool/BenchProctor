// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

const BenchmarkTest00600 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00600 };
