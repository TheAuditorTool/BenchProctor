// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00549(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00549 };
