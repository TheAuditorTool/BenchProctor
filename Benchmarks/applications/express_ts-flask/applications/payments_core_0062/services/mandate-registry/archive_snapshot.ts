// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveSnapshot = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(headline);
  const disbursement: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(disbursement)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = disbursement;
  childProcess.spawn("echo " + remittance, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
