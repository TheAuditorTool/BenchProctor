// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function renderProfile(req, res) {
  const footnote = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(footnote);
  const bulletin = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(bulletin) + "</section>"); return;
}

module.exports = { renderProfile };
