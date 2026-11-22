// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00041 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = userInput != null ? userInput : '';
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00041 };
