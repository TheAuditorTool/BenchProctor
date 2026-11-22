// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00247 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00247 };
