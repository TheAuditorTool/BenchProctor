// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function fetchRecord(req, res) {
  const snippet = req.body?.field || "";
  const _raw = snippet;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(addendum));
}

module.exports = { fetchRecord };
