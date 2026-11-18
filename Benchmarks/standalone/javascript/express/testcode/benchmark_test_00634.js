// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00634(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00634 };
