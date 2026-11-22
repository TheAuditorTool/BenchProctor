// SPDX-License-Identifier: Apache-2.0

async function verifyBatch(req, res) {
  const remark = req.body || "";
  const persona = await Promise.resolve(remark).then(String);
  const axios = require("axios");
  const outbound = { method: "get", url: String(persona), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { verifyBatch };
