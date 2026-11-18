// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00593(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = nodeUtil.format("%s", userInput);
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00593 };
