// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

const BenchmarkTest00299 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  stream.Readable.from([String(data)]).pipe(crypto.createCipheriv("aes-256-ecb", blockKey, null)).pipe(fs.createWriteStream("/var/data/cipher.bin"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00299 };
