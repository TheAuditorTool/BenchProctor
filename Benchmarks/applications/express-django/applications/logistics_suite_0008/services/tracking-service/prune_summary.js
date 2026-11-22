// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function pruneSummary(req, res) {
  const caption = req.body.field || "";
  const _raw = caption;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(consignment));
}

module.exports = { pruneSummary };
