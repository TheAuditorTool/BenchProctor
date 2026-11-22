// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const stream = require("node:stream");

const BenchmarkTest00030 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00030 };
