// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00207 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00207 };
