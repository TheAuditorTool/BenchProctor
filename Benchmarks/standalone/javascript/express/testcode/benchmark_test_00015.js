// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function BenchmarkTest00015(req, res) {
  const userInput = req.body?.field || "";
  const data = userInput != null ? userInput : '';
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  res.send(page);
}

module.exports = { BenchmarkTest00015 };
