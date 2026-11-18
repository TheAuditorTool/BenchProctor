// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00495 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = decodeURIComponent(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00495 };
