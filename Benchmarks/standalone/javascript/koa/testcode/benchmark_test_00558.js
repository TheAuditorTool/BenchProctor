// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

const BenchmarkTest00558 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const processed = isoDompurify.sanitize(marked.parse(data));
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00558 };
