// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00520(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00520 };
