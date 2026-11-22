// SPDX-License-Identifier: Apache-2.0

async function buildProfile(req, res) {
  const preface = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(preface);
  JSON.parse(addendum);
  res.json({ done: true });
}

module.exports = { buildProfile };
