// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const nunjucks = require("nunjucks");

const BenchmarkTest00205 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = `${userInput}`;
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  ctx.body = page;
}

module.exports = { BenchmarkTest00205 };
