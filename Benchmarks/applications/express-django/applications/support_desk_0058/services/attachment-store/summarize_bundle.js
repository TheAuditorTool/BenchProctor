// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function summarizeBundle(req, res) {
  const snippet = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(snippet);
  const inquiry = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(inquiry) + "</section>"); return;
}

module.exports = { summarizeBundle };
