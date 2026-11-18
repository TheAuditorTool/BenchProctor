// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00037 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  res.send("<div>" + data + "</div>");
}
