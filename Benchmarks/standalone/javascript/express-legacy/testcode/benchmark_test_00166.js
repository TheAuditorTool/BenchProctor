// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00166(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + processed + "</section>"); return;
}

module.exports = { BenchmarkTest00166 };
