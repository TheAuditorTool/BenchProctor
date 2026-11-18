// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00559 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00559 };
