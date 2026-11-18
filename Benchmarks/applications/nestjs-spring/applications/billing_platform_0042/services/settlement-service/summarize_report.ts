// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("settlement-service")
export class SummarizeReport {
  @Post("summarizeReport")
  async summarizeReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const remittance: string = transform(remark);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [remittance] });
    return { created: true };
  }
}
