// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function fetchRoster(req, res) {
  const citation = req.body?.field || "";
  const _raw = citation;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(parcel));
}

module.exports = { fetchRoster };
