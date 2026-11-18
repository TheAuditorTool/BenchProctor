// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00107(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = nodeUtil.format("%s", userInput);
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00107 };
