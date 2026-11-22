// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

const BenchmarkTest00260 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00260 };
