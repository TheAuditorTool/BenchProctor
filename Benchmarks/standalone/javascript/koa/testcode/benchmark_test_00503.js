// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

const BenchmarkTest00503 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00503 };
