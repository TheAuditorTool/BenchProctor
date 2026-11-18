// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00054(req, res) {
  const userInput = req.query.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00054 };
