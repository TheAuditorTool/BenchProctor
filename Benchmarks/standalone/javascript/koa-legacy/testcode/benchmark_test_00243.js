// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00243 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00243 };
