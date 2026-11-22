// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00095(req, res) {
  const userInput = req.headers.referer || "";
  const data = decodeURIComponent(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00095 };
