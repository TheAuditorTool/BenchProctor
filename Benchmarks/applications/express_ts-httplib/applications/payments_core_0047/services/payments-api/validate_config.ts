// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const remittance: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  childProcess.exec("echo " + disbursement, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
