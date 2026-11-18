// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00529 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  libxmljs.parseXml(userInput, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
