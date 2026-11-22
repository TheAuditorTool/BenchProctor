// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const fs = require("fs");

const BenchmarkTest00341 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _sk = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
  const _siv = crypto.randomBytes(12);
  const _scipher = crypto.createCipheriv("aes-256-gcm", _sk, _siv);
  const _sct = Buffer.concat([_scipher.update(String(data), "utf8"), _scipher.final()]);
  const _stag = _scipher.getAuthTag();
  fs.writeFileSync("/var/data/cipher.bin", Buffer.concat([_siv, _stag, _sct]));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00341 };
