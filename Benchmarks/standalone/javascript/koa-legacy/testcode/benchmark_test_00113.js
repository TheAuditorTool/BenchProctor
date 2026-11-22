// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00113 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const [data] = String(userInput).split(',');
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00113 };
