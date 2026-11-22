// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00321 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  ctx.body = page;
}

module.exports = { BenchmarkTest00321 };
