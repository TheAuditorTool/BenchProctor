// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00466 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = `${userInput}`;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00466 };
