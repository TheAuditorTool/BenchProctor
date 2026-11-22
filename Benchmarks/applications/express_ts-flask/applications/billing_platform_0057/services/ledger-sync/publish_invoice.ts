// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const publishInvoice = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const remittance: string = normalize(caption);
  const dunning = "/var/app/data/" + path.basename(remittance);
  const fileContent = fs.readFileSync(dunning, "utf8");
  res.send(fileContent);
}
