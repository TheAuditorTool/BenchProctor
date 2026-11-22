// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

const BenchmarkTest00194 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00194 };
