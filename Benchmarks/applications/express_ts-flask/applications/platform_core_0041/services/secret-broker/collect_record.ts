// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.referer as string) || "";
  const payload = { get value() { return passage; } };
  const persona = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
  res.send(fileContent);
}
