// SPDX-License-Identifier: Apache-2.0

async function annotateSummary(req, res) {
  const remark = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(remark);
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { annotateSummary };
