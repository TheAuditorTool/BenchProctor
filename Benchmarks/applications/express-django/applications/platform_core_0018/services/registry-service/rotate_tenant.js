// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function rotateTenant(req, res) {
  const subtitle = req.query.id || "";
  const persona = decodeURIComponent(subtitle);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [persona] });
  res.json({ done: true });
}

module.exports = { rotateTenant };
