// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00578 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(userInput));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00578 };
