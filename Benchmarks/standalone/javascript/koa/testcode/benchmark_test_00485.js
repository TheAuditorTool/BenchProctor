// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00485 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00485 };
