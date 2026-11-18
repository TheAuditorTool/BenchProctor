// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const compactSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const remark = String(preface).replace(/\u0000/g, "");
  res.send("<div>" + remark + "</div>");
}
