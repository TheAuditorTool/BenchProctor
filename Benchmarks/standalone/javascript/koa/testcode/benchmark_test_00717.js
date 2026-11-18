// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00717 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const [data] = String(userInput).split(',');
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00717 };
