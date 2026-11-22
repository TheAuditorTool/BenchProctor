// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function exportPolicy(req, res) {
  const blurb = req.body.field || "";
  const _raw = blurb;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(inquiry));
}

module.exports = { exportPolicy };
