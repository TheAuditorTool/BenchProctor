// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const validateTaxonomy = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const payload = { get value() { return remark; } };
  const byline = payload.value;
  const reportSpec = jsYaml.load(String(byline), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
