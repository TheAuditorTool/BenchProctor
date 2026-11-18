// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00065 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00065 };
