// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");

const BenchmarkTest00105 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00105 };
