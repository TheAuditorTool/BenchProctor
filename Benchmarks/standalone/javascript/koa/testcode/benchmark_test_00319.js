// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");
const stream = require("node:stream");

const BenchmarkTest00319 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00319 };
