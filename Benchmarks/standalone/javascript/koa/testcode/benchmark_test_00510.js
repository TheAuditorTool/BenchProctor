// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

const BenchmarkTest00510 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = nodeUtil.format("%s", userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00510 };
