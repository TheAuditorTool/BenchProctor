// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

async function reconcileComment(req, res) {
  const caption = req.headers["x-custom-header"] || "";
  const synopsis = nodeUtil.format("%s", caption);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: synopsis });
  res.send(page);
}

module.exports = { reconcileComment };
