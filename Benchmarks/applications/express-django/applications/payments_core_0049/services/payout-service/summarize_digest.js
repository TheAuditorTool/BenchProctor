// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function summarizeDigest(req, res) {
  const headline = req.query.id || "";
  const disbursement = decodeURIComponent(headline);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [disbursement] });
  res.json({ done: true });
}

module.exports = { summarizeDigest };
