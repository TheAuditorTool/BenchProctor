// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00152(req, res) {
  const userInput = req.headers.host || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00152 };
