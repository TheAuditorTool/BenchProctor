// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function buildReport(req, res) {
  const notice = req.headers.authorization || "";
  const _raw = notice;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(persona));
}

module.exports = { buildReport };
