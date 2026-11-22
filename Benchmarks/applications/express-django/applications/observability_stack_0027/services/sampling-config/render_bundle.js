// SPDX-License-Identifier: Apache-2.0

async function renderBundle(req, res) {
  const remark = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(remark);
  JSON.parse(gauge);
  res.json({ done: true });
}

module.exports = { renderBundle };
