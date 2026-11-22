// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00042 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = userInput != null ? userInput : '';
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00042 };
