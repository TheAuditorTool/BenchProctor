// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00270(req, res) {
  const userInput = req.body?.multipart_field || "";
  const data = nodeUtil.format("%s", userInput);
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00270 };
