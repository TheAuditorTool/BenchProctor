// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00486(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00486 };
