// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function summarizePolicy(req, res) {
  const paragraph = req.body?.field || "";
  const _raw = paragraph;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(persona));
}

module.exports = { summarizePolicy };
