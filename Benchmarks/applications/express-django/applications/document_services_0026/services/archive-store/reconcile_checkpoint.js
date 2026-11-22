// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function reconcileCheckpoint(req, res) {
  const preface = req.body?.field || "";
  const _raw = preface;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(addendum));
}

module.exports = { reconcileCheckpoint };
