// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function collectSample(req, res) {
  const remark = req.body.payload || "";
  let gauge;
  try { gauge = JSON.parse(remark).value || ""; }
  catch (e) { gauge = String(remark); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: cohort });
  res.send(page);
}

module.exports = { collectSample };
