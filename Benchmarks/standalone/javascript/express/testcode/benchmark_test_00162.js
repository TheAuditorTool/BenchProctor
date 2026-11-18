// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00162(req, res) {
  const userInput = req.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00162 };
