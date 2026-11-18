// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00240 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00240 };
