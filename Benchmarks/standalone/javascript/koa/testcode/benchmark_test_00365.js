// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

const BenchmarkTest00365 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00365 };
