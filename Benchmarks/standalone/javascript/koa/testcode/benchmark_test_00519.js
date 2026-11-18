// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00519 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00519 };
