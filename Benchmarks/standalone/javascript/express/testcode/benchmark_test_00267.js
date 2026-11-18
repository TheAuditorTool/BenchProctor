// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00267(req, res) {
  const userInput = req.body.payload || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00267 };
