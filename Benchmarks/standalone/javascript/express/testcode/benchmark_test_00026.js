// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00026(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = decodeURIComponent(userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00026 };
