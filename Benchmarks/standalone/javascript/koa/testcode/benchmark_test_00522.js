// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00522 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  crypto.createHash("md5").update(userInput).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00522 };
