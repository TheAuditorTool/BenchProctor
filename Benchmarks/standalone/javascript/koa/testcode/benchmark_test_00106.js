// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

const BenchmarkTest00106 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00106 };
