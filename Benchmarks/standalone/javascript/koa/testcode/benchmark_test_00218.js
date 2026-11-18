// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00218 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = userInput != null ? userInput : '';
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00218 };
