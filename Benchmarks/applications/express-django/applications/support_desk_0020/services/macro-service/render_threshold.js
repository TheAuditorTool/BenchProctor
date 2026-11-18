// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function renderThreshold(req, res) {
  const phrase = req.headers.authorization || "";
  const _raw = phrase;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(inquiry));
}

module.exports = { renderThreshold };
