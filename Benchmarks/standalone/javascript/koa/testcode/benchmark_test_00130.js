// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00130 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = `${userInput}`;
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00130 };
