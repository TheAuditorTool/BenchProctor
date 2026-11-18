// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditRoster = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.authorization as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(memo);
  childProcess.execSync("echo " + voucher);
  res.json({ accepted: true });
}
