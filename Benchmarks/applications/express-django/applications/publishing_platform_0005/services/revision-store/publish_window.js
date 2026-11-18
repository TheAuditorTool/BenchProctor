// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function publishWindow(req, res) {
  const footnote = req.headers.authorization || "";
  const _raw = footnote;
  const byline = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(byline));
}

module.exports = { publishWindow };
