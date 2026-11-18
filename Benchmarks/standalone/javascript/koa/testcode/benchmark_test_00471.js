// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00471 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = decodeURIComponent(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00471 };
