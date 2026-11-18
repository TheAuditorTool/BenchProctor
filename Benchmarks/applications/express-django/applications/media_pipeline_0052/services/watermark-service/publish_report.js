// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function publishReport(req, res) {
  const tagline = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: tagline });
  const rendition = formData.payload;
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  net.connect(80, new URL(String(montage)).hostname);
  res.json({ done: true });
}

module.exports = { publishReport };
