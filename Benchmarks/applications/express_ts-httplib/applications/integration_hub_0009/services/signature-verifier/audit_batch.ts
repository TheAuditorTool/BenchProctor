// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const auditBatch = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body as string) || "";
  const handshake = heading != null ? heading : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const remark = handshake;
  res.send("<div>" + remark + "</div>");
}
