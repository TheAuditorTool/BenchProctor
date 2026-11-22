// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00348(req, res) {
  const userInput = req.headers.referer || "";
  const data = nodeUtil.format("%s", userInput);
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00348 };
