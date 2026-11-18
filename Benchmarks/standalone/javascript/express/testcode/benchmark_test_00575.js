// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00575(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00575 };
