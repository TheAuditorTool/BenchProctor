// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactSchedule(req, res) {
  const paragraph = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(paragraph);
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const cohort = gauge;
  const axios = require("axios");
  const outbound = { method: "get", url: String(cohort), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { compactSchedule };
