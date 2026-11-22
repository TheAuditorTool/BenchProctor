// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function formatRedaction(req, res) {
  const phrase = req.body?.payload || "";
  let dossier;
  try { dossier = JSON.parse(phrase).value || ""; }
  catch (e) { dossier = String(phrase); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(dossier)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: addendum });
  res.send(page);
}

module.exports = { formatRedaction };
