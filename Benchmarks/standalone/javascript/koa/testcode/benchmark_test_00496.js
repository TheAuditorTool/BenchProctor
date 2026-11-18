// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");

const BenchmarkTest00496 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00496 };
