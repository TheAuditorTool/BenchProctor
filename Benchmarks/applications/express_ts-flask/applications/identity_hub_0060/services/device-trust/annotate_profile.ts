// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateProfile = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.query.id as string) || "";
  const [persona] = String(paragraph).split(',');
  childProcess.exec("echo " + persona, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
