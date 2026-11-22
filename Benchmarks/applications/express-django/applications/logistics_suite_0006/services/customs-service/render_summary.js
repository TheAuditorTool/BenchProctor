// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function renderSummary(req, res) {
  const summary = req.query.id || "";
  const formData = Object.freeze({ payload: summary });
  const consignment = formData.payload;
  http.get(consignment);
  res.json({ done: true });
}

module.exports = { renderSummary };
