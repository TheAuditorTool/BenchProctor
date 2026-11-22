// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.query.id as string) || "";
  const [dossier] = String(phrase).split(',');
  childProcess.exec("echo " + dossier, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
