// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function buildSnapshot(req, res) {
  const synopsis = req.body.payload || "";
  let byline;
  try { byline = JSON.parse(synopsis).value || ""; }
  catch (e) { byline = String(synopsis); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}

module.exports = { buildSnapshot };
