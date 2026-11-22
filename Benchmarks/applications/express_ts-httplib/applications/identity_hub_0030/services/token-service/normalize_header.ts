// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const normalizeHeader = async (req: Request, res: Response): Promise<void> => {
  const tagline = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(tagline);
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const note = persona;
  net.connect(80, new URL(String(note)).hostname);
  res.json({ accepted: true });
}
