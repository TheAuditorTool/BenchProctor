// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const pruneConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  let consignment;
  try { consignment = JSON.parse(footnote).value || footnote; }
  catch (e) { consignment = footnote; }
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ accepted: true });
}
