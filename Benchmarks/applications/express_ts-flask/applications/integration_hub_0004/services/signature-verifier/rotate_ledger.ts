// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.cookies?.session_token as string) || "";
  const _raw = summary;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  childProcess.exec("echo " + paragraph, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
