// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateAlert = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.query.id as string) || "";
  const [cohort] = String(excerpt).split(',');
  childProcess.exec("echo " + cohort, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
