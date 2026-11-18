// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00189 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  fs.unlinkSync("/var/app/data/" + userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00189 };
