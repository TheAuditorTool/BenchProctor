// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00449(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  crypto.createHash("md5").update(userInput).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00449 };
