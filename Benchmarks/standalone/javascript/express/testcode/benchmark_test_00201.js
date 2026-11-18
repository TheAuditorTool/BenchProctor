// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function BenchmarkTest00201(req, res) {
  const userInput = req.body.field || "";
  const data = userInput != null ? userInput : '';
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00201 };
