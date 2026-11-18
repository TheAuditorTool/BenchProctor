// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const reconcileAsset = async (req: Request, res: Response): Promise<void> => {
  const notice = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(notice);
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  http.get(montage);
  res.json({ accepted: true });
}
