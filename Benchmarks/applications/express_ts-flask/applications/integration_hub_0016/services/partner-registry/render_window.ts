// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as jsYaml from "js-yaml";

export const renderWindow = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.referer as string) || "";
  const payload = { get value() { return wording; } };
  const handshake = payload.value;
  const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
