// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00648(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00648 };
