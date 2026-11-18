// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const archiveSurvey = async (req: Request, res: Response): Promise<void> => {
  const citation = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(citation);
  res.send("<div>" + grievance + "</div>");
}
