// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function formatWindow(req, res) {
  const wording = (req.file && req.file.originalname) || "";
  const [remark] = String(wording).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(remark)));
  res.json({ done: true });
}

module.exports = { formatWindow };
