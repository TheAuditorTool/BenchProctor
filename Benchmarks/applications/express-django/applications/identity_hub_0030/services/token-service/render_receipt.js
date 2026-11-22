// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function renderReceipt(req, res) {
  const tagline = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(tagline);
  const persona = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(persona) + "</section>"); return;
}

module.exports = { renderReceipt };
