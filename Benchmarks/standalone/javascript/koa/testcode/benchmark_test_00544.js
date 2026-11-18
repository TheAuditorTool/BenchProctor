// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00544 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00544 };
