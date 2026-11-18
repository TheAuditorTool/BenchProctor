// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const normalizeDocument = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.host as string) || "";
  const synopsis = `${remark}`;
  let _host = "";
  try { _host = new URL(String(synopsis)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const quotation = synopsis;
  http.get(quotation);
  res.json({ accepted: true });
}
