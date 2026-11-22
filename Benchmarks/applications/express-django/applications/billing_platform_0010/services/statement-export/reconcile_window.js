// SPDX-License-Identifier: Apache-2.0

async function reconcileWindow(req, res) {
  const headline = req.body || "";
  const remittance = await Promise.resolve(headline).then(String);
  const axios = require("axios");
  const outbound = { method: "get", url: String(remittance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { reconcileWindow };
