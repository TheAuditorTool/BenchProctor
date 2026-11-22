// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00224 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = `${userInput}`;
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00224 };
