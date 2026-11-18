// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateIndex = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const persona = decodeURIComponent(phrase);
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
