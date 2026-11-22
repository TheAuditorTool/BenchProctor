// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00320 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00320 };
