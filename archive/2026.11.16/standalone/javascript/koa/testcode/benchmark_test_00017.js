// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00017 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00017 };
