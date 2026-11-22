// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function compactIndex(req, res) {
  const tagline = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(tagline);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: persona });
  res.send(page);
}

module.exports = { compactIndex };
