// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00575 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00575 };
