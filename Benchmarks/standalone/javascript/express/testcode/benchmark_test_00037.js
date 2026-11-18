// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00037(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00037 };
