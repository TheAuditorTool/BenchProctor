// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00268(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  new Function("return (" + String(data) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00268 };
