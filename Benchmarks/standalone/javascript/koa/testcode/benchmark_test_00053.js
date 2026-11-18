// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00053 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00053 };
