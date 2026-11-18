// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { Sequelize } from "sequelize";

export const BenchmarkTest00682 = async (req: Request, res: Response): Promise<void> => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
