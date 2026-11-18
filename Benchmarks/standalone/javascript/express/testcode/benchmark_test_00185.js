// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00185(req, res) {
  const userInput = req.query.id || "";
  const data = decodeURIComponent(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00185 };
