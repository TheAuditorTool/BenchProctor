// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const auditProfile = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.origin as string) || "";
  const [remittance] = String(footnote).split(',');
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const arrears = remittance;
  const outbound = { method: "get", url: String(arrears), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
