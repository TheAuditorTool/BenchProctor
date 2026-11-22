// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00105 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00105 };
