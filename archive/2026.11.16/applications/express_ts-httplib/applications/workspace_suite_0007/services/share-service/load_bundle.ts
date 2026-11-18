// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const loadBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const subtitle: string = readInput();
  let _host = "";
  try { _host = new URL(String(subtitle)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = subtitle;
  http.get(notice);
  res.json({ accepted: true });
}
