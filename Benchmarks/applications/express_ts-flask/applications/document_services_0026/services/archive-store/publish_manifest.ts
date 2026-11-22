// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const payload = { get value() { return preface; } };
  const addendum = payload.value;
  const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
