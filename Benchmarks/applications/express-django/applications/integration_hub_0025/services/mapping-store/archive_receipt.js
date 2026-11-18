// SPDX-License-Identifier: Apache-2.0

async function archiveReceipt(req, res) {
  const footnote = req.body.payload || "";
  const _raw = footnote;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const blurb = handshake;
  res.send("<div>" + blurb + "</div>");
}

module.exports = { archiveReceipt };
