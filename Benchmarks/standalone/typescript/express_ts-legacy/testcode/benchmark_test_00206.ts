// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as jsYaml from "js-yaml";

export const BenchmarkTest00206 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}
