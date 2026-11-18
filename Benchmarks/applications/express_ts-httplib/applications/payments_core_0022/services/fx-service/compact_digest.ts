// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactDigest = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.params.id as string) || "";
  const ledger = decodeURIComponent(subject);
  childProcess.execSync("echo " + ledger);
  res.json({ accepted: true });
}
