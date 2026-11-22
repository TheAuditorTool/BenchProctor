// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadReceipt = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.params.id as string) || "";
  const handshake = decodeURIComponent(heading);
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
