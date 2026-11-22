// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateHeader = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const consignment: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(consignment)) { res.status(403).json({error:'forbidden'}); return; }
  const parcel = consignment;
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
