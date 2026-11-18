// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00287(req, res) {
  const userInput = req.params.id || "";
  const data = userInput != null ? userInput : '';
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00287 };
