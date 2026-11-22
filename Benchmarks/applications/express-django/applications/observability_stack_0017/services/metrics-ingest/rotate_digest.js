// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function rotateDigest(req, res) {
  const note = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(note);
  const cohort = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(cohort) + "</section>"); return;
}

module.exports = { rotateDigest };
