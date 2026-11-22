// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = ((req as any).files?.[0]?.originalname as string) || "";
  const addendum = String(transcript).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  http.get(byline);
  res.json({ accepted: true });
}
