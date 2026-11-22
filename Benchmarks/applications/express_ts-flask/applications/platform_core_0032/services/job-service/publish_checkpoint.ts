// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.field as string) || "";
  const [persona] = String(remark).split(',');
  const reportSpec = jsYaml.load(String(persona), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
