// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as ldapjs from "ldapjs";
import * as joi from "joi";

export const BenchmarkTest00129 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.#%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  res.json({ accepted: true });
}
