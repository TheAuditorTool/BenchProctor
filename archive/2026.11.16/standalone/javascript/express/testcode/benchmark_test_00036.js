// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00036(req, res) {
  const userInput = req.headers.host || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00036 };
