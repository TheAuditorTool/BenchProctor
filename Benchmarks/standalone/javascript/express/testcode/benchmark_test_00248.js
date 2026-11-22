// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00248(req, res) {
  const userInput = req.body?.payload || "";
  const [data] = String(userInput).split(',');
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00248 };
