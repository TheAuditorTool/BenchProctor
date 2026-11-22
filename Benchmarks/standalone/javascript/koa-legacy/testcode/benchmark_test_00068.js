// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

const BenchmarkTest00068 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = nodeUtil.format("%s", userInput);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  ctx.body = page;
}

module.exports = { BenchmarkTest00068 };
