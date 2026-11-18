// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00566 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00566 };
