// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function publishCheckpoint(req, res) {
  const preface = req.body.payload || "";
  let bulletin;
  try { bulletin = JSON.parse(preface).value || ""; }
  catch (e) { bulletin = String(preface); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const citation = bulletin;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: citation });
  res.send(page);
}

module.exports = { publishCheckpoint };
