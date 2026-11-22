// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

const BenchmarkTest00159 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00159 };
