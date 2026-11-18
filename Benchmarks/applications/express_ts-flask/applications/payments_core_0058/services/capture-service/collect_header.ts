// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectHeader = async (req: Request, res: Response): Promise<void> => {
  const caption = process.env.PAYMENTS_INPUT_0058 || "";
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(caption);
  childProcess.execSync("echo " + ledger);
  res.json({ accepted: true });
}
