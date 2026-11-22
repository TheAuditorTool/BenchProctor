// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00205 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  ctx.body = page;
}

module.exports = { BenchmarkTest00205 };
