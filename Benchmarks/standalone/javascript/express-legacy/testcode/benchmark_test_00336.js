// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nunjucks = require("nunjucks");

async function BenchmarkTest00336(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = nodeUtil.format("%s", userInput);
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}

module.exports = { BenchmarkTest00336 };
