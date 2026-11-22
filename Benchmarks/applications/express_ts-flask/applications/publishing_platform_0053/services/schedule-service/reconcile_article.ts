// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const reconcileArticle = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const payload = { get value() { return note; } };
  const byline = payload.value;
  const reportSpec = jsYaml.load(String(byline), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
