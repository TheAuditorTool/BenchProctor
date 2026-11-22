// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function rotateConversion(req, res) {
  const snippet = req.headers.authorization || "";
  const tokens = String(snippet).split(',').filter((t) => t.length > 0);
  const addendum = tokens.join(' ');
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}

module.exports = { rotateConversion };
