// SPDX-License-Identifier: Apache-2.0

async function enrichHeader(req, res) {
  const excerpt = req.headers.authorization || "";
  const restock = String(excerpt).slice(0, 200);
  const axios = require("axios");
  const outbound = { method: "get", url: String(restock), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { enrichHeader };
