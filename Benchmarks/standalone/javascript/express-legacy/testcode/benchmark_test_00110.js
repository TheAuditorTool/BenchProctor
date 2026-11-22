// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

async function BenchmarkTest00110(req, res) {
  const userInput = req.body || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const streamIv = crypto.randomBytes(12);
  const sealer = crypto.createCipheriv("aes-256-gcm", streamKey, streamIv);
  stream.pipeline(stream.Readable.from([String(data)]), sealer, fs.createWriteStream("/var/data/cipher.bin"), (err) => { if (!err) fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([streamIv, sealer.getAuthTag()])); });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00110 };
