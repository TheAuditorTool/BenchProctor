// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function compactProfile(req, res) {
  const notice = req.headers.authorization || "";
  let persona;
  try { persona = JSON.parse(notice).value || notice; }
  catch (e) { persona = notice; }
  nodeSerialize.unserialize(persona);
  res.json({ done: true });
}

module.exports = { compactProfile };
