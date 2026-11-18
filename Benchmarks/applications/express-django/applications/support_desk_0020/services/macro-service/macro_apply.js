// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function applyMacro(req, res) {
  const phrase = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const inquiry = String(phrase).replace(/\u0000/g, "");
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://survey-service:8000/send_survey", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { applyMacro };
