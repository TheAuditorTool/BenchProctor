// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00032 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = userInput != null ? userInput : '';
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00032 };
