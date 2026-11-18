// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00617(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = nodeUtil.format("%s", userInput);
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00617 };
