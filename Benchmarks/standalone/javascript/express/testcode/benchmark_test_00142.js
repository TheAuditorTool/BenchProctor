// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00142(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00142 };
