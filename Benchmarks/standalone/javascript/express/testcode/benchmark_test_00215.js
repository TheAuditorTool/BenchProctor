// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00215(req, res) {
  const userInput = req.headers.authorization || "";
  const data = nodeUtil.format("%s", userInput);
  res.redirect(data);
}

module.exports = { BenchmarkTest00215 };
