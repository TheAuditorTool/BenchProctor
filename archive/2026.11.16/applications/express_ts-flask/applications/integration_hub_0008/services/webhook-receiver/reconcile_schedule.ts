// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcileSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(preface);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  childProcess.execSync("echo " + paragraph);
  res.json({ accepted: true });
}
