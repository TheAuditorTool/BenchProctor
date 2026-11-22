// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichRoster = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const parcel: string = normalize(quotation);
  const consignment = "/var/app/data/" + path.basename(parcel);
  const fileContent = fs.readFileSync(consignment, "utf8");
  res.send(fileContent);
}
