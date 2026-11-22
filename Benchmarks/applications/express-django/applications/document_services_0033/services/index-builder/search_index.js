// SPDX-License-Identifier: Apache-2.0

async function indexDocument(req, res) {
  const snippet = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(snippet);
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ done: true });
}

module.exports = { indexDocument };
