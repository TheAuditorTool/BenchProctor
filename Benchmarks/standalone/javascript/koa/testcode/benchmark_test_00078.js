// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00078 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = `${userInput}`;
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00078 };
