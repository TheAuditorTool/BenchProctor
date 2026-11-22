// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00225 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  ctx.body = page;
}

module.exports = { BenchmarkTest00225 };
