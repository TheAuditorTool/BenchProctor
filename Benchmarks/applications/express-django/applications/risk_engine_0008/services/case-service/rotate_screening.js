// SPDX-License-Identifier: Apache-2.0

async function rotateScreening(req, res) {
  const synopsis = req.body.payload || "";
  const _raw = synopsis;
  const verdict = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(verdict))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  res.send("<div>" + grievance + "</div>");
}

module.exports = { rotateScreening };
