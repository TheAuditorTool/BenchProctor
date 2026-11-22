// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function summarizeCheckpoint(req, res) {
  const heading = req.body?.field || "";
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(handshake));
}

module.exports = { summarizeCheckpoint };
