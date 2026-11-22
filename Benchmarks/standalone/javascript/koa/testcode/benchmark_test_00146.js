// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00146 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "hex").toString();
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00146 };
