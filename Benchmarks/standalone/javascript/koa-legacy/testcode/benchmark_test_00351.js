// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00351 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = decodeURIComponent(userInput);
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00351 };
