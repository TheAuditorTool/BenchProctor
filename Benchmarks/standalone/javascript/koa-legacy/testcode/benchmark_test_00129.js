// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00129 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00129 };
