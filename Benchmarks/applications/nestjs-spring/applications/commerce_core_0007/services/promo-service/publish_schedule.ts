// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("promo-service")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const voucher: string = transform(heading);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [voucher] });
    return { created: true };
  }
}
