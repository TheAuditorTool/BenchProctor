// SPDX-License-Identifier: Apache-2.0

async function collectSchedule(req, res) {
  const preface = req.body.payload || "";
  const _raw = preface;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { res.status(400).json({error:"invalid"}); return; }
  const notice = bulletin;
  res.send("<div>" + notice + "</div>");
}

module.exports = { collectSchedule };
