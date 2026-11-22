// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00323 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00323 };
