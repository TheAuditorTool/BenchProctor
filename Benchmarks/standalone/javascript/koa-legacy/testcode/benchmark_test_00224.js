// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");
const stream = require("node:stream");

const BenchmarkTest00224 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00224 };
