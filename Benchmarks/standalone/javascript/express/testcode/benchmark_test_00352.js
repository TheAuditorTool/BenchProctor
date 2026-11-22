// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

async function BenchmarkTest00352(req, res) {
  const userInput = req.body?.multipart_field || "";
  const data = `${userInput}`;
  const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  const streamIv = crypto.randomBytes(8);
  fs.writeFileSync("/var/data/cipher.iv", streamIv);
  stream.pipeline(stream.Readable.from([String(data)]), crypto.createCipheriv("des-ede3-cbc", streamKey, streamIv), fs.createWriteStream("/var/data/cipher.bin"), (err) => { if (err) console.error("encryption failed", err); });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00352 };
