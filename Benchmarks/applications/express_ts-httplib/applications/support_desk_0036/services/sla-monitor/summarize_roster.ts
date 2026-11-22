// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const summarizeRoster = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(preface);
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ accepted: true });
}
