// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const note = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(note);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  http.get(dossier);
  res.json({ accepted: true });
}
