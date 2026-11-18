// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditWindow = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const parcel = decodeURIComponent(phrase);
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
