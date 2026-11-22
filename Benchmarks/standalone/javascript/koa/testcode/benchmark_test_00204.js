// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

const BenchmarkTest00204 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  stream.Readable.from([String(data)]).pipe(crypto.createCipheriv("aes-256-ecb", blockKey, null)).pipe(fs.createWriteStream("/var/data/cipher.bin"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00204 };
