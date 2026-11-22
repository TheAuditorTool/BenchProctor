// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function BenchmarkTest00331(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
  res.send(page);
}

module.exports = { BenchmarkTest00331 };
