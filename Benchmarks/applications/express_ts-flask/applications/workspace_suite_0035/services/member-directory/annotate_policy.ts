// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const annotatePolicy = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.referer as string) || "";
  const payload = { get value() { return paragraph; } };
  const wording = payload.value;
  const reportSpec = jsYaml.load(String(wording), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
