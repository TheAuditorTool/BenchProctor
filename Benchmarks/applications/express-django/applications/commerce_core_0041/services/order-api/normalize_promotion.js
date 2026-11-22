// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizePromotion(req, res) {
  const headline = req.headers.host || "";
  const backorder = `${headline}`;
  http.get(backorder);
  res.json({ done: true });
}

module.exports = { normalizePromotion };
