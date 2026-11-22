// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00023(req, res) {
  const userInput = req.query.id || "";
  crypto.createHash("md5").update(userInput).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00023 };
