// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const annotateReport = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(passage);
  res.send("<div>" + remittance + "</div>");
}
