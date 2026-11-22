// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { PrismaClient } from "@prisma/client";

export const annotateReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(remark);
  const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + gauge + "'");
  res.json({ accepted: true });
}
