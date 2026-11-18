// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00505 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00505 };
