// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00294 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00294 };
