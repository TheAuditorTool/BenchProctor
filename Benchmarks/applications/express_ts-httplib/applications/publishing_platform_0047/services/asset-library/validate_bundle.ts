// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const synopsis = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const byline: string = transform(synopsis);
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = byline;
  http.get(addendum);
  res.json({ accepted: true });
}
