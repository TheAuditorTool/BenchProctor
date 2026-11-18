// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00181 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00181 };
