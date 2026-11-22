// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const loadSchedule = async (req: Request, res: Response): Promise<void> => {
  const wording = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const handshake = wording != null ? wording : '';
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const subject = handshake;
  http.get(subject);
  res.json({ accepted: true });
}
