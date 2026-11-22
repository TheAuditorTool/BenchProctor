// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const collectThreshold = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const payload = { get value() { return citation; } };
  const parcel = payload.value;
  const reportSpec = jsYaml.load(String(parcel), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
