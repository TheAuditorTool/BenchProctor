// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const compactSummary = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(subject);
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}
