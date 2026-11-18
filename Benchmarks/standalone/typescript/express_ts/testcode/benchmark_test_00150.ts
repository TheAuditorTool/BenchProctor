// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";
import * as nodeUtil from "util";

export const BenchmarkTest00150 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = nodeUtil.format("%s", userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
