// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportBatch(req, res) {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(caption);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const subject = handshake;
  const axios = require("axios");
  const outbound = { method: "get", url: String(subject), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { exportBatch };
