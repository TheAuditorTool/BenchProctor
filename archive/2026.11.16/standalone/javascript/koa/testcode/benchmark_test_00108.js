// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00108 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00108 };
