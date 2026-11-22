// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00225 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00225 };
