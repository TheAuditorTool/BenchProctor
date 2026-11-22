// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function archiveEscalation(req, res) {
  const phrase = req.body.field || "";
  const _raw = phrase;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(grievance));
}

module.exports = { archiveEscalation };
