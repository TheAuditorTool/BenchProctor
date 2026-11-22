// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function rotateMacro(req, res) {
  const preface = req.body?.field || "";
  const _raw = preface;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(grievance));
}

module.exports = { rotateMacro };
