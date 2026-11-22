// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

async function renderPolicy(req, res) {
  const memo = req.headers["x-custom-header"] || "";
  const verdict = nodeUtil.format("%s", memo);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: verdict });
  res.send(page);
}

module.exports = { renderPolicy };
