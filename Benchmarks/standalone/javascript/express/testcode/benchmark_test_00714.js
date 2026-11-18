// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00714(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00714 };
