// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00620(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00620 };
