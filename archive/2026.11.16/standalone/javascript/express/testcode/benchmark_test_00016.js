// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00016(req, res) {
  const userInput = req.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00016 };
