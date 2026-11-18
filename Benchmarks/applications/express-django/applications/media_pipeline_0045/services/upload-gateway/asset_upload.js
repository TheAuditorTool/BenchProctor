// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function uploadAsset(req, res) {
  const notice = req.headers["user-agent"] || "";
  const rendition = nodeUtil.format("%s", notice);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://transcode-service:8000/enqueue_transcode", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ done: true });
}

module.exports = { uploadAsset };
