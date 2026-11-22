// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00077(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}

module.exports = { BenchmarkTest00077 };
