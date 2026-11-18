// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00224 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00224 };
