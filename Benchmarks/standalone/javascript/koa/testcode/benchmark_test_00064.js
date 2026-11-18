// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00064 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00064 };
