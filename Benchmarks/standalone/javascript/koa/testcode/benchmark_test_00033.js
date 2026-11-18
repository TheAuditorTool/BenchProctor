// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00033 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00033 };
