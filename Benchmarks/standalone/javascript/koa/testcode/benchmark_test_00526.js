// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00526 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00526 };
