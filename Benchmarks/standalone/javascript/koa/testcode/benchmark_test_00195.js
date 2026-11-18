// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00195 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00195 };
