// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00138 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).slice(0, 200);
  const _desKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  crypto.createCipheriv("des-ede3-ecb", _desKey, null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00138 };
