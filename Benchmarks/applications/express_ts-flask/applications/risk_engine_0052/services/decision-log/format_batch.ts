// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatBatch = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(memo);
  const fileContent = fs.readFileSync("/var/app/data/" + verdict, "utf8");
  res.send(fileContent);
}
