// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const BenchmarkTest00357 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
