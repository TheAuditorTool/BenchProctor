// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function renderIndex(req, res) {
  const summary = req.headers.authorization || "";
  const _raw = summary;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(addendum));
}

module.exports = { renderIndex };
