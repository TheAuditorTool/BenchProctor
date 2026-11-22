// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneReceipt = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(phrase);
  const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
  res.send(fileContent);
}
