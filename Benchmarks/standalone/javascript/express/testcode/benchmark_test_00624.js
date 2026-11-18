// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00624(req, res) {
  const userInput = req.headers.authorization || "";
  const data = nodeUtil.format("%s", userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00624 };
