// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00035 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00035 };
