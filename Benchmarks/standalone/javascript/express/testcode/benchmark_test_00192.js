// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00192(req, res) {
  const userInput = req.query.id || "";
  const data = nodeUtil.format("%s", userInput);
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00192 };
