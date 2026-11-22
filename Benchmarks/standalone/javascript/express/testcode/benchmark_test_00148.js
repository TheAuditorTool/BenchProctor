// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function BenchmarkTest00148(req, res) {
  const userInput = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}

module.exports = { BenchmarkTest00148 };
