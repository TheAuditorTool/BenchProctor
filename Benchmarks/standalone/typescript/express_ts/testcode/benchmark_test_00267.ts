// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { Sequelize } from "sequelize";

export const BenchmarkTest00267 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  res.json({ accepted: true });
}
