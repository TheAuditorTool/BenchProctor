// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

async function BenchmarkTest00055(req, res) {
  const userInput = req.body || "";
  const data = nodeUtil.format("%s", userInput);
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00055 };
