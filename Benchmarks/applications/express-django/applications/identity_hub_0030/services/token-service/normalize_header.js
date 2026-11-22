// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function normalizeHeader(req, res) {
  const tagline = req.body.payload || "";
  let persona;
  try { persona = JSON.parse(tagline).value || ""; }
  catch (e) { persona = String(tagline); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const note = persona;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: note });
  res.send(page);
}

module.exports = { normalizeHeader };
