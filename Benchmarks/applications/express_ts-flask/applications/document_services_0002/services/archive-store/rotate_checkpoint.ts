// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const wording = ((req as any).files?.[0]?.originalname as string) || "";
  const addendum = String(wording).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  http.get(dossier);
  res.json({ accepted: true });
}
