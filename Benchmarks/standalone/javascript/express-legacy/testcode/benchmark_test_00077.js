// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function BenchmarkTest00077(req, res) {
  const userInput = req.body || "";
  const [data] = String(userInput).split(',');
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}

module.exports = { BenchmarkTest00077 };
