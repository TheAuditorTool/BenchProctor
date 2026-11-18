// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileSnapshot = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const payload = { get value() { return caption; } };
  const cohort = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + cohort, "utf8");
  res.send(fileContent);
}
