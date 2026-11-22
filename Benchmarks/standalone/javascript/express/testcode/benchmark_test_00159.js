// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");
const stream = require("node:stream");

async function BenchmarkTest00159(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).slice(0, 200);
  const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const blockIv = crypto.randomBytes(12);
  const sealer = crypto.createCipheriv("aes-256-gcm", blockKey, blockIv);
  stream.Readable.from([String(data)]).pipe(sealer).pipe(fs.createWriteStream("/var/data/cipher.bin")).on("finish", () => fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([blockIv, sealer.getAuthTag()])));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00159 };
