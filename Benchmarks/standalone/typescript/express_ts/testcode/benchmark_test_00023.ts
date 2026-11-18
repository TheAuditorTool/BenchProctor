// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const BenchmarkTest00023 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
