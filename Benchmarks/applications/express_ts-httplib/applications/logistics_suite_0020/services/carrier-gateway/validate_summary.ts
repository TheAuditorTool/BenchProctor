// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const validateSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(transcript);
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ accepted: true });
}
