// SPDX-License-Identifier: Apache-2.0
const nunjucks = require("nunjucks");

async function fetchConfig(req, res) {
  const synopsis = req.body?.payload || "";
  let rendition;
  try { rendition = JSON.parse(synopsis).value || ""; }
  catch (e) { rendition = String(synopsis); }
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: montage });
  res.send(page);
}

module.exports = { fetchConfig };
