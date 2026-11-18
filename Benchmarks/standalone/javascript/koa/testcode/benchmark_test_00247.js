// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00247 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = userInput != null ? userInput : '';
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00247 };
