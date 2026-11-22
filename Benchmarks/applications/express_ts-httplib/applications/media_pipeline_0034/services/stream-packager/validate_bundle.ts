// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const synopsis = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const rendition = synopsis != null ? synopsis : '';
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  http.get(montage);
  res.json({ accepted: true });
}
