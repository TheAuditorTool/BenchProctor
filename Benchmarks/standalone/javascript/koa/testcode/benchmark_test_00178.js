// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

const BenchmarkTest00178 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = Buffer.from(userInput, "base64").toString();
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00178 };
