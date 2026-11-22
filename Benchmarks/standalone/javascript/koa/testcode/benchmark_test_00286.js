// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

const BenchmarkTest00286 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00286 };
