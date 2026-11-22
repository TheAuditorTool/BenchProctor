// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const BenchmarkTest00357 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
