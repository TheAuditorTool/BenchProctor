// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00047(req, res) {
  const userInput = req.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00047 };
