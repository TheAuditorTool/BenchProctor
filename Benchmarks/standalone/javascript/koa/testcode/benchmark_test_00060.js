// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

const BenchmarkTest00060 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00060 };
