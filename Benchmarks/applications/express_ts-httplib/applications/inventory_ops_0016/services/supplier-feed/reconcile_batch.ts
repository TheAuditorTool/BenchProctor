// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.multipart_field as string) || "";
  let backorder;
  try { backorder = JSON.parse(citation).value || citation; }
  catch (e) { backorder = citation; }
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const restock = backorder;
  net.connect(80, new URL(String(restock)).hostname);
  res.json({ accepted: true });
}
