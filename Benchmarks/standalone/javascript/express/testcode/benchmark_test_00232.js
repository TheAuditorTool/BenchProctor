// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00232(req, res) {
  const userInput = req.headers.origin || "";
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(userInput));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00232 };
