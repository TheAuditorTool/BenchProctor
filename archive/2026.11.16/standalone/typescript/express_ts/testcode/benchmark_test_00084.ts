// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const BenchmarkTest00084 = async (req: Request, res: Response): Promise<void> => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ accepted: true });
}
