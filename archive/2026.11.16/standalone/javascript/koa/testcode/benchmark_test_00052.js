// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00052 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00052 };
