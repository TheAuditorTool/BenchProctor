// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");
const nodeUtil = require("util");

const BenchmarkTest00046 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = nodeUtil.format("%s", userInput);
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00046 };
