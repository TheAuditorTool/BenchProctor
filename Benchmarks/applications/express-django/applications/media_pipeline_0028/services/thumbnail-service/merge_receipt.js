// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function mergeReceipt(req, res) {
  const citation = req.params.id || "";
  const _raw = citation;
  const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: rendition });
  res.send(page);
}

module.exports = { mergeReceipt };
