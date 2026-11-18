// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00103 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
