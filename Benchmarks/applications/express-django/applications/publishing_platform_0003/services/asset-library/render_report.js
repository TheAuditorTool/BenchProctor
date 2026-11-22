// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function renderReport(req, res) {
  const heading = req.body?.payload || "";
  let addendum;
  try { addendum = JSON.parse(heading).value || ""; }
  catch (e) { addendum = String(heading); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: byline });
  res.send(page);
}

module.exports = { renderReport };
