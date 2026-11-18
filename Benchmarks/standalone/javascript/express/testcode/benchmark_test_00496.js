// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00496(req, res) {
  const userInput = req.body || "";
  const data = nodeUtil.format("%s", userInput);
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00496 };
