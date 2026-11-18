// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00652(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = nodeUtil.format("%s", userInput);
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00652 };
