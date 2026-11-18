// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function BenchmarkTest00717(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00717 };
