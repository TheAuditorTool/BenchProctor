// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00310 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  crypto.createHash("sha256").update(userInput).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00310 };
