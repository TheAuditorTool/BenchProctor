// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const BenchmarkTest00262 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const [data] = String(userInput).split(',');
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ accepted: true });
}
