// SPDX-License-Identifier: Apache-2.0

async function mergeMandate(req, res) {
  const headline = req.body || "";
  const disbursement = await Promise.resolve(headline).then(String);
  const axios = require("axios");
  const outbound = { method: "get", url: String(disbursement), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { mergeMandate };
