// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00039 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00039 };
