// SPDX-License-Identifier: Apache-2.0

async function archiveRecord(req, res) {
  const remark = req.headers.authorization || "";
  const _raw = remark;
  const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + remittance + "</div>");
}

module.exports = { archiveRecord };
