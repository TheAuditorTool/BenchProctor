// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00156 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).replace(/\u0000/g, "");
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00156 };
