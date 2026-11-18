// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00283(req, res) {
  const userInput = req.body.payload || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00283 };
