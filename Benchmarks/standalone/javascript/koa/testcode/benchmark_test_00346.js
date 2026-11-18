// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00346 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = decodeURIComponent(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00346 };
