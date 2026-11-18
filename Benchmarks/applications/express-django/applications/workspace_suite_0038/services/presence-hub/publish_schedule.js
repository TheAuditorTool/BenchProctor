// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

async function publishSchedule(req, res) {
  const preface = req.headers.authorization || "";
  const _raw = preface;
  const remark = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send(escapeHtml(remark));
}

module.exports = { publishSchedule };
