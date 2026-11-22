// SPDX-License-Identifier: Apache-2.0

async function indexDocument(req, res) {
  const footnote = req.params.id || "";
  const _raw = footnote;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ done: true });
}

module.exports = { indexDocument };
