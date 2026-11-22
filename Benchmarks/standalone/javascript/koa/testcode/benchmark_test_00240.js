// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00240 = async (ctx) => {
  const userInput = ctx.query.id || "";
  crypto.createHash("md5").update(userInput).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00240 };
