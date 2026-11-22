// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00221(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = nodeUtil.format("%s", userInput);
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00221 };
