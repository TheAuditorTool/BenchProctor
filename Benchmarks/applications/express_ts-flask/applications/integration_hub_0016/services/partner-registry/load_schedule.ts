// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadSchedule = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.params.id as string) || "";
  const handshake = decodeURIComponent(wording);
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  childProcess.execSync("echo " + subject);
  res.json({ accepted: true });
}
