// SPDX-License-Identifier: Apache-2.0
const stream = require("node:stream");
const { escapeHtml } = require("./shared");

const BenchmarkTest00030 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + escapeHtml(data) + "</section>"]);
}

module.exports = { BenchmarkTest00030 };
