// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function scheduleJob(req, res) {
  const notice = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = notice;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://feature-flags:8000/evaluate_flag", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { scheduleJob };
