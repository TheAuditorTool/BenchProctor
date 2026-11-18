// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00054 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = userInput != null ? userInput : '';
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00054 };
