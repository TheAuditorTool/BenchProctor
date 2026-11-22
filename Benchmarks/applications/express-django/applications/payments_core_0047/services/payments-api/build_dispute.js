// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function buildDispute(req, res) {
  const footnote = req.body?.payload || "";
  let remittance;
  try { remittance = JSON.parse(footnote).value || ""; }
  catch (e) { remittance = String(footnote); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: disbursement });
  res.send(page);
}

module.exports = { buildDispute };
