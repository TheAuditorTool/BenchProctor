// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const annotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.origin as string) || "";
  const [backorder] = String(memo).split(',');
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const restock = backorder;
  const outbound = { method: "get", url: String(restock), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
