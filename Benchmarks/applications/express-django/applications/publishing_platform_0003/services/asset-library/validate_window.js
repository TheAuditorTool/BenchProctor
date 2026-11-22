// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function validateWindow(req, res) {
  const heading = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(heading);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}

module.exports = { validateWindow };
