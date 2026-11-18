// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00646(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = `${userInput}`;
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00646 };
