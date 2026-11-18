// SPDX-License-Identifier: Apache-2.0

async function mergeHeader(req, res) {
  const preface = req.body.payload || "";
  const _raw = preface;
  const remark = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(remark))) { res.status(400).json({error:"invalid"}); return; }
  const wording = remark;
  res.send("<div>" + wording + "</div>");
}

module.exports = { mergeHeader };
