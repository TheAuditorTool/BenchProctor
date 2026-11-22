// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

const BenchmarkTest00097 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const streamIv = crypto.randomBytes(12);
  const sealer = crypto.createCipheriv("aes-256-gcm", streamKey, streamIv);
  stream.pipeline(stream.Readable.from([String(data)]), sealer, fs.createWriteStream("/var/data/cipher.bin"), (err) => { if (!err) fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([streamIv, sealer.getAuthTag()])); });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00097 };
