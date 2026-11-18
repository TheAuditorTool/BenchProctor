// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00371 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const [data] = String(userInput).split(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00371 };
