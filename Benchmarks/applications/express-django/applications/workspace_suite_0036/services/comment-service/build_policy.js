// SPDX-License-Identifier: Apache-2.0

async function buildPolicy(req, res) {
  const remark = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const synopsis = trim(remark);
  res.send("<div>" + synopsis + "</div>");
}

module.exports = { buildPolicy };
