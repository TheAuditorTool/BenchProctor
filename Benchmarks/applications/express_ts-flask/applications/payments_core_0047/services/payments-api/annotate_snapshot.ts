// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

export const annotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body?.field as string) || "";
  const [remittance] = String(footnote).split(',');
  const reportSpec = jsYaml.load(String(remittance), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
