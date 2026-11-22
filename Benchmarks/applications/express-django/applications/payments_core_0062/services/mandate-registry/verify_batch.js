// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function verifyBatch(req, res) {
  const headline = req.query.id || "";
  const formData = Object.freeze({ payload: headline });
  const disbursement = formData.payload;
  http.get(disbursement);
  res.json({ done: true });
}

module.exports = { verifyBatch };
