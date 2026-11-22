// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00139 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00139 };
