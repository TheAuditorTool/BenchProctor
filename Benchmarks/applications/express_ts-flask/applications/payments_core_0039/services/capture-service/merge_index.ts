// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const mergeIndex = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.referer as string) || "";
  const payload = { get value() { return memo; } };
  const ledger = payload.value;
  const reportSpec = jsYaml.load(String(ledger), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
