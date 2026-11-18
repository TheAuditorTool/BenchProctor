// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";

export const BenchmarkTest00459 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const _clean = isoDompurify.sanitize(data);
  const processed = _clean;
  res.send("<div>" + processed + "</div>");
}
