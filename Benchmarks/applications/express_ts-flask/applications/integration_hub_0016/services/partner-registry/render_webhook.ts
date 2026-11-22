// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

export const renderWebhook = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body?.field as string) || "";
  const [handshake] = String(wording).split(',');
  const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
