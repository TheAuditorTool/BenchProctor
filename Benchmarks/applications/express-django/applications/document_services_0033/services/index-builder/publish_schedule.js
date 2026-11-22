// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function publishSchedule(req, res) {
  const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(snippet);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  const axios = require("axios");
  const outbound = { method: "get", url: String(dossier), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { publishSchedule };
