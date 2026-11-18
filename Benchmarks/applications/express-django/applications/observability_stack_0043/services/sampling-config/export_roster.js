// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function exportRoster(req, res) {
  const note = req.headers.authorization || "";
  const _raw = note;
  const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(gauge));
}

module.exports = { exportRoster };
