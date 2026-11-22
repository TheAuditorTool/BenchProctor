// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00012 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00012 };
