// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00641 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00641 };
