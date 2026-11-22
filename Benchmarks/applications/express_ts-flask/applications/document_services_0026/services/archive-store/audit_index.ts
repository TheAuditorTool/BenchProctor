// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

export const auditIndex = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.field as string) || "";
  const [addendum] = String(preface).split(',');
  const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
