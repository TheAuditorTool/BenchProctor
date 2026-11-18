// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

const BenchmarkTest00515 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = userInput != null ? userInput : '';
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00515 };
