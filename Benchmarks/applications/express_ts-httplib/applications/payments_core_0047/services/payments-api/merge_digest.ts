// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const mergeDigest = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(footnote);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const disbursement = remittance;
  net.connect(80, new URL(String(disbursement)).hostname);
  res.json({ accepted: true });
}
