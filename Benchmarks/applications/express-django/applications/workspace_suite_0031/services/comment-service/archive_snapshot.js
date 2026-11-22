// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function archiveSnapshot(req, res) {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const synopsis = normalize(caption);
  let _host = "";
  try { _host = new URL(String(synopsis)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const snippet = synopsis;
  const axios = require("axios");
  const outbound = { method: "get", url: String(snippet), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { archiveSnapshot };
