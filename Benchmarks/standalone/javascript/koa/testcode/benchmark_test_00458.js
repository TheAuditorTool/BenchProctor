// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00458 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00458 };
