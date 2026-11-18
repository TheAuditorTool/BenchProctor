// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00013(req, res) {
  const userInput = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00013 };
