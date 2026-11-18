// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00374 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = decodeURIComponent(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00374 };
