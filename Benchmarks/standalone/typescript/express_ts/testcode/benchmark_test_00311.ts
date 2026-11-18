// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeSerialize from "node-serialize";

export const BenchmarkTest00311 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
