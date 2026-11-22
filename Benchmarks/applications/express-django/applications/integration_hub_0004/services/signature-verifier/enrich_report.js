// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function enrichReport(req, res) {
  const summary = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(summary);
  const handshake = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(handshake) + "</section>"); return;
}

module.exports = { enrichReport };
