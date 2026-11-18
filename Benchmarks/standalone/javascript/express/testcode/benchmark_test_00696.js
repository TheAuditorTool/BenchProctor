// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00696(req, res) {
  const userInput = req.body.field || "";
  const data = decodeURIComponent(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00696 };
