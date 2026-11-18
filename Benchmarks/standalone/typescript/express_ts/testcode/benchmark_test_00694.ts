// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as ldapjs from "ldapjs";

export const BenchmarkTest00694 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = userInput != null ? userInput : '';
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + data + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  res.json({ accepted: true });
}
