// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00121(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00121 };
