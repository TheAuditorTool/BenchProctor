// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00665 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00665 };
