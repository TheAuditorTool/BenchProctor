// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function auditPolicy(req, res) {
  const preface = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(preface);
  const grievance = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(grievance) + "</section>"); return;
}

module.exports = { auditPolicy };
