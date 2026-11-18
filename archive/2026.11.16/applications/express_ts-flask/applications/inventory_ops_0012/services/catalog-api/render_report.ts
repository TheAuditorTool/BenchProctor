// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.host as string) || "";
  const backorder = `${phrase}`;
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const restock = backorder;
  http.get(restock);
  res.json({ accepted: true });
}
