// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function collectManifest(req, res) {
  const citation = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const consignment = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(consignment) + "</section>"); return;
}

module.exports = { collectManifest };
