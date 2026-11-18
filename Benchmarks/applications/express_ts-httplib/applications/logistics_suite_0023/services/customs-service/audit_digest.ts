// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditDigest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const parcel: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(parcel)) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
