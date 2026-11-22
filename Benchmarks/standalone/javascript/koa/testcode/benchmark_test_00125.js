// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00125 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  ctx.body = page;
}

module.exports = { BenchmarkTest00125 };
