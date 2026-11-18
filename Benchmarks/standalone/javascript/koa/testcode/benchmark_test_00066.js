// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

const BenchmarkTest00066 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.writeFileSync(checkedPath, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00066 };
