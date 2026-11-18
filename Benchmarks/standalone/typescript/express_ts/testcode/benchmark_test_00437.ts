// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00437 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  libxmljs.parseXml(userInput, { noent: true, dtdload: true, nonet: false } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
