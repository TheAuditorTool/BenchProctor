// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const renderHeader = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.referer as string) || "";
  const payload = { get value() { return headline; } };
  const backorder = payload.value;
  const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
