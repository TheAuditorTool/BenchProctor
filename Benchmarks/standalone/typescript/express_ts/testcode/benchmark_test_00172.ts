// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00172 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
