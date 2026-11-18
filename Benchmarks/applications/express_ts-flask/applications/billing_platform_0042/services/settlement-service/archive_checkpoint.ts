// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const archiveCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const payload = { get value() { return remark; } };
  const remittance = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
  res.send(fileContent);
}
