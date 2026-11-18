// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00440 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00440 };
