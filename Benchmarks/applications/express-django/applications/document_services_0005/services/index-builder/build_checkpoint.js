// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function buildCheckpoint(req, res) {
  const footnote = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(footnote);
  const addendum = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(addendum) + "</section>"); return;
}

module.exports = { buildCheckpoint };
