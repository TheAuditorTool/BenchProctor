// SPDX-License-Identifier: Apache-2.0

async function storeArchive(req, res) {
  const preface = req.params.id || "";
  let addendum;
  const onInput = (v) => { addendum = v; };
  onInput(preface);
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ done: true });
}

module.exports = { storeArchive };
