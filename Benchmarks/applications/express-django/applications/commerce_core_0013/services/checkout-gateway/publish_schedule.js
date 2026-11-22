// SPDX-License-Identifier: Apache-2.0

async function publishSchedule(req, res) {
  const wording = req.cookies.session_token || "";
  const backorder = Buffer.from(wording, "base64").toString();
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ done: true });
}

module.exports = { publishSchedule };
