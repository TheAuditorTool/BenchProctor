// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function normalizeRoster(req, res) {
  const summary = req.headers.authorization || "";
  const _raw = summary;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(grievance));
}

module.exports = { normalizeRoster };
