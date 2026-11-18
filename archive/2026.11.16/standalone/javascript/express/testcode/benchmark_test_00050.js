// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00050(req, res) {
  const userInput = req.body.payload || "";
  const data = nodeUtil.format("%s", userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00050 };
