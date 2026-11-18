// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const formatBundle = async (req: Request, res: Response): Promise<void> => {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const backorder = String(citation).replace(/\u0000/g, "");
  res.send("<div>" + backorder + "</div>");
}
