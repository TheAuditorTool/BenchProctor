// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00182 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = `${userInput}`;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  ctx.body = page;
}

module.exports = { BenchmarkTest00182 };
