// SPDX-License-Identifier: Apache-2.0

async function enrichSchedule(req, res) {
  const synopsis = req.headers.authorization || "";
  const rendition = String(synopsis).slice(0, 200);
  const axios = require("axios");
  const outbound = { method: "get", url: String(rendition), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { enrichSchedule };
