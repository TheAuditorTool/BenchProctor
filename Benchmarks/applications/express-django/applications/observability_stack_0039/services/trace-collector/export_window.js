// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function exportWindow(req, res) {
  const caption = req.headers.authorization || "";
  const _raw = caption;
  const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(cohort));
}

module.exports = { exportWindow };
