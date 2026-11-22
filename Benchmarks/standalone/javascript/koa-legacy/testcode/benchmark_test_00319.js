// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00319 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const [data] = String(userInput).split(',');
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  ctx.body = page;
}

module.exports = { BenchmarkTest00319 };
