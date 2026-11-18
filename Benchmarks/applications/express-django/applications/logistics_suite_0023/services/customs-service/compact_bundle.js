// SPDX-License-Identifier: Apache-2.0

async function compactBundle(req, res) {
  const caption = req.headers.authorization || "";
  const _raw = caption;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + parcel + "</div>");
}

module.exports = { compactBundle };
