// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const BenchmarkTest00086 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = userInput != null ? userInput : '';
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ accepted: true });
}
