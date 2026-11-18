// SPDX-License-Identifier: Apache-2.0

async function resolveProfile(req, res) {
  const passage = req.body.payload || "";
  const _raw = passage;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  res.send("<div>" + addendum + "</div>");
}

module.exports = { resolveProfile };
