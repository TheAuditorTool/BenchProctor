// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const rotateConfig = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const ledger: string = normalize(memo);
  const remittance = "/var/app/data/" + path.basename(ledger);
  const fileContent = fs.readFileSync(remittance, "utf8");
  res.send(fileContent);
}
