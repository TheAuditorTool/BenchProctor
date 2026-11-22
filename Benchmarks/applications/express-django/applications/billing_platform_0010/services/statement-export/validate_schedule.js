// SPDX-License-Identifier: Apache-2.0

async function validateSchedule(req, res) {
  const headline = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(headline);
  JSON.parse(remittance);
  res.json({ done: true });
}

module.exports = { validateSchedule };
