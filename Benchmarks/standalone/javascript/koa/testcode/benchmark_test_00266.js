// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00266 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00266 };
