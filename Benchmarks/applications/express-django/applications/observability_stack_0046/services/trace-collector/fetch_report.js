// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function fetchReport(req, res) {
  const paragraph = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(paragraph);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: gauge });
  res.send(page);
}

module.exports = { fetchReport };
