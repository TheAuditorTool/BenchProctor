// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function buildWaybill(req, res) {
  const summary = req.body.field || "";
  const _raw = summary;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(consignment));
}

module.exports = { buildWaybill };
