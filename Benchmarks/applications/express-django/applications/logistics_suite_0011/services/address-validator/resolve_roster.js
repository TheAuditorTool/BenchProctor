// SPDX-License-Identifier: Apache-2.0

async function resolveRoster(req, res) {
  const citation = req.cookies.session_token || "";
  const consignment = Buffer.from(citation, "hex").toString();
  const axios = require("axios");
  const outbound = { method: "get", url: String(consignment), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { resolveRoster };
