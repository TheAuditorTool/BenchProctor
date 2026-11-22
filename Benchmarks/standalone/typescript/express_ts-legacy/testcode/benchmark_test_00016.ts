// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";

export const BenchmarkTest00016 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ accepted: true });
}
