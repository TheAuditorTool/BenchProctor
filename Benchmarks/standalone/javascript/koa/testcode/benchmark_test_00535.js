// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00535 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00535 };
