// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00720 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00720 };
