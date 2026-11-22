// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00216 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00216 };
