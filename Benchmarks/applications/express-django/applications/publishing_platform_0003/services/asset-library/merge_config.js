// SPDX-License-Identifier: Apache-2.0

async function mergeConfig(req, res) {
  const heading = req.body || "";
  const addendum = await Promise.resolve(heading).then(String);
  const axios = require("axios");
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { mergeConfig };
