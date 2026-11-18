// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditHeader = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const handshake: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
