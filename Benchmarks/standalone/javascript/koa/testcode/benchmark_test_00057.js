// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

const BenchmarkTest00057 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = userInput != null ? userInput : '';
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  ctx.body = page;
}

module.exports = { BenchmarkTest00057 };
