// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00129(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00129 };
