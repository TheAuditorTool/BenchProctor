// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.referer as string) || "";
  const payload = { get value() { return transcript; } };
  const backorder = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
  res.send(fileContent);
}
