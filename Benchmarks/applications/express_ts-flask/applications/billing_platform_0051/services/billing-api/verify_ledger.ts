// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyLedger = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const arrears: string = normalize(synopsis);
  childProcess.execSync("echo " + arrears);
  res.json({ accepted: true });
}
