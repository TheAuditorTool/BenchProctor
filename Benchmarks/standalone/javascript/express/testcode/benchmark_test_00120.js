// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function BenchmarkTest00120(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = `${userInput}`;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}

module.exports = { BenchmarkTest00120 };
