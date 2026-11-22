// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const vm = require("node:vm");

async function BenchmarkTest00183(req, res) {
  const userInput = req.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  vm.runInNewContext(String(parsedNum), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00183 };
