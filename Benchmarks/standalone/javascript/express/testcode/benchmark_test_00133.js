// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00133(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00133 };
