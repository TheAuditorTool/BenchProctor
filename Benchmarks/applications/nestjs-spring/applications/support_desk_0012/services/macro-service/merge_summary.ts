// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("macro-service")
export class MergeSummary {
  @Post("mergeSummary")
  async mergeSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(summary);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [grievance] });
    return { created: true };
  }
}
