// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const BenchmarkTest00653 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  res.json({ accepted: true });
}
