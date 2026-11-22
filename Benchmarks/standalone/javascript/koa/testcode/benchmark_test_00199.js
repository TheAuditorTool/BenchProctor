// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00199 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00199 };
