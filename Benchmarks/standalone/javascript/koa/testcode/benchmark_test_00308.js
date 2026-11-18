// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00308 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00308 };
