// SPDX-License-Identifier: Apache-2.0

async function renderAsset(req, res) {
  const citation = req.headers.origin || "";
  const rendition = String(citation).slice(0, 200);
  JSON.parse(rendition);
  res.json({ done: true });
}

module.exports = { renderAsset };
