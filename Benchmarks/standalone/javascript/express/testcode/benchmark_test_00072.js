// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00072(req, res) {
  const userInput = req.body.payload || "";
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00072 };
