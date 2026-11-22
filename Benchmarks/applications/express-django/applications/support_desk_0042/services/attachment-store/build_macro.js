// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

async function buildMacro(req, res) {
  const blurb = req.headers["x-custom-header"] || "";
  const inquiry = nodeUtil.format("%s", blurb);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: inquiry });
  res.send(page);
}

module.exports = { buildMacro };
