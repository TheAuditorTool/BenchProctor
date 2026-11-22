// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

async function summarizeLedger(req, res) {
  const summary = req.headers["x-custom-header"] || "";
  const handshake = nodeUtil.format("%s", summary);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: handshake });
  res.send(page);
}

module.exports = { summarizeLedger };
