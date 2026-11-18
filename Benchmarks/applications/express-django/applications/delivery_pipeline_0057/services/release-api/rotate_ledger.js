// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function rotateLedger(req, res) {
  const footnote = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: footnote });
  const wording = formData.payload;
  let _host = "";
  try { _host = new URL(String(wording)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const note = wording;
  net.connect(80, new URL(String(note)).hostname);
  res.json({ done: true });
}

module.exports = { rotateLedger };
