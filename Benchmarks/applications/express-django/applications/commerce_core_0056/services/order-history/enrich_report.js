// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function enrichReport(req, res) {
  const citation = req.headers.authorization || "";
  const _raw = citation;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(backorder));
}

module.exports = { enrichReport };
