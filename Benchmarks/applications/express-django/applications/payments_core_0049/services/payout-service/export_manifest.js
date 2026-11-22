// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function exportManifest(req, res) {
  const headline = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(headline);
  const disbursement = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(disbursement) + "</section>"); return;
}

module.exports = { exportManifest };
