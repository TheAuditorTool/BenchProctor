// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00129 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00129 };
