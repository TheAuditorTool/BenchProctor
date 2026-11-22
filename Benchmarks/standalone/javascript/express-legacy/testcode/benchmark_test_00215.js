// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00215(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00215 };
