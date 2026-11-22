// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function auditLedger(req, res) {
  const synopsis = req.query.id || "";
  const formData = Object.freeze({ payload: synopsis });
  const byline = formData.payload;
  http.get(byline);
  res.json({ done: true });
}

module.exports = { auditLedger };
