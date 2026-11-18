// SPDX-License-Identifier: Apache-2.0

async function validateBundle(req, res) {
  const note = req.body.payload || "";
  const _raw = note;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  res.send("<div>" + grievance + "</div>");
}

module.exports = { validateBundle };
