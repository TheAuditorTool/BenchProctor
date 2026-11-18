// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00088 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
