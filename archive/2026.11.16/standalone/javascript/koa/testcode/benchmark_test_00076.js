// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00076 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const [data] = String(userInput).split(',');
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00076 };
