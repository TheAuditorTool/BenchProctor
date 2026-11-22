// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function mergeProfile(req, res) {
  const remark = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(remark);
  const persona = readInput();
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + escapeHtml(persona) + "</section>"); return;
}

module.exports = { mergeProfile };
