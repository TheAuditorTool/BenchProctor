// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function rotateBundle(req, res) {
  const headline = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const disbursement = normalize(headline);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: disbursement });
  res.send(page);
}

module.exports = { rotateBundle };
