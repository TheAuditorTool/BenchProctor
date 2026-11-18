// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00416 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
