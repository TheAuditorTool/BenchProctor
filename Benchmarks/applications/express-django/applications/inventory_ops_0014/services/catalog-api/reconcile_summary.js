// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function reconcileSummary(req, res) {
  const excerpt = req.body.field || "";
  const _raw = excerpt;
  const restock = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(restock));
}

module.exports = { reconcileSummary };
