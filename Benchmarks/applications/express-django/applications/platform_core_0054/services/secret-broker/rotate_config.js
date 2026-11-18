// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function rotateConfig(req, res) {
  const snippet = req.headers.authorization || "";
  const _raw = snippet;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(persona));
}

module.exports = { rotateConfig };
