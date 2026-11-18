// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");

async function BenchmarkTest00485(req, res) {
  const userInput = req.headers.authorization || "";
  const data = `${userInput}`;
  const _sk = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY || "").digest();
  const _siv = crypto.randomBytes(12);
  const _scipher = crypto.createCipheriv("aes-256-gcm", _sk, _siv);
  const _sct = Buffer.concat([_scipher.update(String(data), "utf8"), _scipher.final()]);
  const _stag = _scipher.getAuthTag();
  fs.writeFileSync("/var/data/cipher.bin", Buffer.concat([_siv, _stag, _sct]));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00485 };
